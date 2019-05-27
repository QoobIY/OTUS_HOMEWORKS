import sqlite3


def connect():
    conn = sqlite3.connect("products.sqlite")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return cursor, conn


def get_products():
    try:
        cursor, conn = connect()
        cursor.execute('SELECT id,name,description,price FROM products')
        rows = cursor.fetchall()
        conn.close()
        product_dict = [dict(product) for product in rows]
        return product_dict
    except:
        return {}


def get_product(id):
    try:
        cursor, conn = connect()
        cursor.execute('SELECT id,name,description,price FROM products WHERE id={}'.format(id))
        rows = cursor.fetchall()
        conn.close()
        if rows[0]:
            return dict(rows[0])
        return {}
    except:
        return {}
