from orm.base import Base, connect
from orm.orm_field import Field, Foreign
from orm import orm_field


class Author(Base):
    __table__ = 'Author'

    id = Field(orm_field.INT, primary=True)
    name = Field(orm_field.CHAR, maxlength=30)
    pseudonym = Field(orm_field.CHAR, maxlength=30, nullable=True)


class Book(Base):
    __table__ = 'Book'

    id = Field(orm_field.INT, primary=True)
    name = Field(orm_field.CHAR, maxlength=50)
    author = Foreign(Author, nullable=False)


open('test.sqlite', 'w')
connect('test.sqlite')

Author().create()
Author().add(id=0, name='Ivan')
Author().add(id=1, name='Petr')
Author().add(id=2, name='Vasily', pseudonym='Goran')
Author().add(id=3, name='Irina')
print(Author().get())
Author().get().to_dict()
Author().get(id=1).update(pseudonym='Azbuka')
Author().get(id=1).to_dict()

Book().create()
Book().add(id=0, name='Book1', author=1)
Book().add(id=1, name='Book2', author=1)
Book().add(id=2, name='Book3', author=2)
Book().add(id=3, name='Book4', author=0)
book = Book().get()
print('book', book.to_dict())
print('author', book.Author.to_dict())
book2 = Book().get(id=3)
print('book', book2.to_dict())
print('author', book2.Author.to_dict())

Book().drop()
