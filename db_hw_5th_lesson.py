import sqlite3

connect = sqlite3.connect('orders.db')
cursor = connect.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            product TEXT,
            quantity INTEGER DEFAULT NULL
        )
""")

def register():
    name = input("Enter your full name: ")
    product = input("Enter your product: ")
    quantity = int(input("Enter quantity of the product: "))

    cursor.execute(""" INSERT INTO orders
                   (name, product, quantity)
                   VALUES (?, ?, ?)""",(name, product, quantity))

register()


def all_products():
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    print(orders)

all_products()

def all_products(id):
    cursor.execute("SELECT * FROM orders WHERE id=?", (id,))
    orders = cursor.fetchone()
    print(orders)

all_products(1)

# def delete_products(id):
#     cursor.execute("DELETE FROM orders WHERE ID = ?", (id,))
#     connect.commit()
#     print(f"The order {id} was deleted succesfully.")

# delete_products(2)

