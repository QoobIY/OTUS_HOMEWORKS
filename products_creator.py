import sqlite3
from random import random

try:
    FILENAME = 'products.sqlite'
    # Пересоздаём базу
    f = open(FILENAME, 'w')

    conn = sqlite3.connect(FILENAME)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE products (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name	varchar ( 50 ),
    description	text,
    price	real
    );
    ''')

    LOREM_ISPUM = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
     sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
     Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
     nisi ut aliquip ex ea commodo consequat.
     Duis aute irure dolor in reprehenderit in
     voluptate velit esse cillum dolore eu fugiat nulla pariatur.
     Excepteur sint occaecat cupidatat non proident,
     sunt in culpa qui officia deserunt mollit anim id est laborum.
     '''

    values = []
    for row_id in range(9):
        values.append("({},'product {}','{}',{})".format(row_id, int(random()*1024),
                                                         LOREM_ISPUM, round(random()*10000), 2))
    cursor.execute("INSERT INTO products (id,name,description,price) VALUES {};".format(",".join(values)))
    conn.commit()
    conn.close()
    print('Успешно создано')
except Exception as e:
    print('Ошибка при создании базы данных')
    print(str(e))
