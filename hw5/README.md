# Sqlite ORM

Self-written ORM for working with the sqlite database

## Usage
**1. Create table class** 

```python
from orm.base import Base
from orm import orm_field


class Table(Base):
    __table__ = 'Table'

    id = Field(orm_field.INT, primary=True)
    name = Field(orm_field.CHAR, maxlength=30)
```
 ##### Field types
 * `INT` - The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
 * `TEXT` - The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
 * `CHAR` - as a `TEXT`, but with fixed size
 * `REAL` - The value is a floating point value, stored as an 8-byte IEEE floating point number.
 ##### Field rules
 * `nullable` - *True* - field can be null, *False* - cannot be null. Default `False`
 * `maxlength` - *0-255*, if type is char , maxlength set length of this field
 * `primary` -  *True* - set field as primary key for table *Table*, *False* - regular field. Default `False`
 
**2. Connect to database**

```python
from orm.base import connect

connect('test.sqlite')
```

**3. Create table**

```python
Table.create()
```

#### Base commands
`Table.create()` create a table based on class data

`Table.get(table_key=value)` select data in table with the ability to filter data

`Table.add(id=data_id,name=data_name)` insert data in table

`Table.get(id=data_old_id).update(name=data_name)` update name for row with id = **data_old_id**.

`Table.drop()` delete table **Table** from database

All basic commands are also presented in file [sqlite_orm_example.py](sqlite_orm_example.py)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
