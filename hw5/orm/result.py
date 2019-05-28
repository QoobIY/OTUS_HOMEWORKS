import sqlite3
from .orm_functions import fields_to_sql_row


class Result:
    def __init__(self, table, data, **kwargs):
        self.data = data
        self.table = table
        if 'foreign_fields' in kwargs and 'foreign_list' in kwargs:
            for field in kwargs['foreign_fields']:
                foreign_keys = field[1].foreign_table().get_keys(named_key=True)
                foreign_list = []
                for row in kwargs['foreign_list']:
                    dict_row = {}
                    for key, value in row.items():
                        if key in foreign_keys:
                            dict_row[key.replace(field[1].foreign_table.__table__+'__', '', 1)] = value
                    foreign_list.append(dict_row)
                setattr(self, field[1].foreign_table.__table__, Result(field[1].foreign_table, foreign_list))

    def to_dict(self):
        return self.data

    def update(self, **kwargs):
        try:
            if not self.table.cursor:
                raise sqlite3.DatabaseError('Need to open session')
            if len(kwargs) == 0:
                raise ValueError('Nothing to update, empty arguments')
            query_base = "UPDATE {} SET".format(self.table.__table__)
            to_set = fields_to_sql_row(kwargs)
            query_base += " {}".format(",".join(to_set))
            for row in self.data:
                query = " WHERE "
                filters = fields_to_sql_row(row)
                query += ' AND '.join(filters)
                # print(query_base+query)
                self.table.cursor.execute(query_base + query)
            self.table.conn.commit()
            return True
        except Exception as e:
            print('Error to update data {}: {}'.format(self.to_dict(), e))
            return False
