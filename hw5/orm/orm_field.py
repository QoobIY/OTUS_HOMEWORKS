CHAR = 'VARCHAR'
INT = 'INTEGER'
TEXT = 'TEXT'
REAL = 'REAL'
ORM_TYPES = [CHAR, INT, TEXT, REAL]


class Field:
    def __init__(self, field_type, **kwargs):
        if field_type not in ORM_TYPES:
            raise TypeError('Enter correct type {}'.format(ORM_TYPES))
        self.primary = 'primary' in kwargs and kwargs['primary'] is True
        self.nullable = 'nullable' in kwargs and kwargs['nullable'] is True
        self.type = field_type
        if field_type == CHAR:
            if 'maxlength' not in kwargs:
                raise NameError('maxlength reqired for CHAR')
            if kwargs['maxlength'] < 0 or kwargs['maxlength'] > 255:
                raise ValueError('maxlength must be between 0 and 255')
            self.maxlength = kwargs['maxlength']

    def type_to_str(self):
        to_str = self.type
        if self.type == CHAR:
            to_str += '({})'.format(self.maxlength)
        if self.primary:
            to_str += ' PRIMARY KEY'
        if not self.nullable:
            to_str += ' NOT NULL'
        return to_str


class Foreign:

    def __init__(self, foreign_table,  **kwargs):
        self.foreign_table = foreign_table
        self.nullable = 'nullable' in kwargs and kwargs['nullable'] is True

    def type_to_str(self):
        field_type = self.foreign_table.__dict__['id'].type
        to_str = '{0}, FOREIGN KEY({{}}) REFERENCES {1}(id)'.format(field_type, self.foreign_table.__table__)
        return to_str
