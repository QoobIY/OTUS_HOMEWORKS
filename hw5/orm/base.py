import sqlite3
from . import orm_field, result
from .orm_functions import fields_to_sql_row


class Base:
    conn = None
    cursor = None

    def _get_fields(self):
        all_fields = self.__class__.__dict__
        orm_fields = []
        for key, field in all_fields.items():
            if isinstance(field, orm_field.Field):
                orm_fields.append((key, field))
        return orm_fields

    def _get_foreign_fields(self):
        all_fields = self.__class__.__dict__
        foreign_fields = []
        for key, field in all_fields.items():
            if isinstance(field, orm_field.Foreign):
                foreign_fields.append((key, field))
        return foreign_fields

    def get_keys(self, table=False, named_key=False):
        all_fields = self.__class__.__dict__
        orm_fields = []
        for key, field in all_fields.items():
            if isinstance(field, orm_field.Field):
                if table:
                    orm_fields.append("{1}.{0} as {1}__{0}".format(key, self.__table__))
                elif named_key:
                    orm_fields.append("{1}__{0}".format(key, self.__table__))
                else:
                    orm_fields.append(key)
        return orm_fields

    def get(self, **kwargs):
        try:
            if not Base.cursor:
                raise sqlite3.DatabaseError('Need to open session')
            foreign_fields = self._get_foreign_fields()
            query_keys = self.get_keys(table=True)
            for field in foreign_fields:
                query_keys.extend(field[1].foreign_table().get_keys(table=True))
            query = 'SELECT {} FROM {}'.format(",".join(query_keys), self.__table__)
            for field in foreign_fields:
                query += ' JOIN {0} ON {1}.{2}={0}.id'.format(field[1].foreign_table.__table__, self.__table__, field[0])
            if len(kwargs) > 0:
                query += ' WHERE '
                filters = fields_to_sql_row(kwargs, self.__table__)
                query += ' AND '.join(filters)
            selected_data = Base.cursor.execute(query).fetchall()
            selected_list = []
            table_keys = self.get_keys(named_key=True)
            foreign_list = []
            for row in selected_data:
                dict_row = {}
                foreign_row = {}
                for key, value in dict(row).items():
                    if key in table_keys:
                        dict_row[key.replace(self.__table__+'__', '', 1)] = value
                    foreign_row[key] = value
                selected_list.append(dict_row)
                if len(foreign_row) > 0:
                    foreign_list.append(foreign_row)
            if len(foreign_fields) == 0:
                return result.Result(self, selected_list)
            return result.Result(self, selected_list, foreign_fields=foreign_fields, foreign_list=foreign_list)
        except Exception as e:
            print('Select fail : {}'.format(e))
            return []

    def create(self):
        try:
            if not Base.cursor:
                raise sqlite3.DatabaseError('Need to open session')
            fields = self._get_fields()
            sqlite_fields = []
            for field in fields:
                sqlite_fields.append('{} {}'.format(field[0], field[1].type_to_str()))
            foreign_fields = self._get_foreign_fields()

            for field in foreign_fields:
                sqlite_fields.append('{} {}'.format(field[0], field[1].type_to_str().format(field[0])))
            query = 'CREATE TABLE {} ({})'.format(self.__table__, ','.join(sqlite_fields))
            # print(query)
            Base.cursor.execute(query)
            Base.conn.commit()
        except sqlite3.OperationalError as err:
            print('Error on creating table: {}'.format(err))
        except Exception as e:
            print('Error on creating table: {}'.format(e))

    def drop(self):
        try:
            if not Base.cursor:
                raise sqlite3.DatabaseError('Need to open session')
            Base.cursor.execute('DROP TABLE {}'.format(self.__table__))
            Base.conn.commit()
        except Exception as e:
            print('Error on deleting table: {}'.format(e))

    def add(self, **kwargs):
        try:
            if len(kwargs) == 0:
                raise Exception('Nothing to add')
            query = 'INSERT INTO {}'.format(self.__table__)
            fields = self._get_fields()
            fields.extend(self._get_foreign_fields())
            keys = []
            values = []
            for field in fields:
                if not field[1].nullable and (field[0] not in kwargs or kwargs[field[0]] is None):
                    raise Exception('Field {} cannot be null'.format(field[0]))
                if field[0] not in kwargs:
                    continue
                value = kwargs[field[0]]
                keys.append(field[0])
                value = '"{}"'.format(value) if type(value) == str else str(value)
                values.append(value)
            query += '({}) VALUES ({})'.format(",".join(keys), ",".join(values))
            # print(query)
            Base.cursor.execute(query)
            Base.conn.commit()
            return True
        except Exception as e:
            print('Error to add data: {}'.format(e))
            return False


def connect(db_name):
    Base.conn = sqlite3.connect(db_name)
    Base.conn.row_factory = sqlite3.Row
    Base.cursor = Base.conn.cursor()
