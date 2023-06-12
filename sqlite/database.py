# sqlite datatypes are:
# NULL: something doesn't exists
# INTEGER: entire numbers
# REAL: decimal numbers
# TEXT: strings
# BLOB: stores as files are (images, mp3, files)

import sqlite3

database_name = 'othercustomers.db'

# We first need to connect to a database
# You can also connect to a database in memory
# conn = sqlite3.connect(':memory:')
def open_connection():
    global conn, cursor
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

def close_connection():
    conn.commit()
    conn.close()

many_customers = [
                    ('Nami', 'no sé', 'nami@op.com', '3158208763'),
                    ('Gecko', 'Moria', 'moria@op.com', '3124494324'),
                    ('Silvers', 'Rayleigh', 'rayreyes@gl.com', '3054434892'),
                ]

# Create a table
def create_table():
    open_connection()
    cursor.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text,
    phone int
    )
    """)
    close_connection()

# 
def insert_data(data):
    open_connection()
    cursor.execute("INSERT INTO customers VALUES (?,?,?,?)", data)
    print('Data added')
    close_connection()

def insertmany_data(many_customers):
    open_connection()
    cursor.executemany("INSERT INTO customers VALUES (?,?,?,?)", many_customers)
    print('Many Data added')
    close_connection()

def query_data():
    open_connection()
    cursor.execute("SELECT * FROM customers")
    # print(cursor.fetchone()[0])
    # print(cursor.fetchmany(2))
    items = cursor.fetchall()
    close_connection()
    print('NAME\t' + 'Email')
    print("---\t" + '---')
    for item in items:
        print(item[0] + "\t" + item[2])
    
def show_rowid():
    open_connection()
    cursor.execute("SELECT rowid, * FROM customers")
    items = cursor.fetchall()
    for item in items:
        print(item)
    close_connection()

def search_by():
    open_connection()
    cursor.execute("SELECT * FROM customers WHERE email LIKE '%wgovt.com'")
    items = cursor.fetchall()
    for item in items:
        print(item)
    close_connection()

def update_record():
    open_connection()
    cursor.execute("""UPDATE customers SET first_name = 'Tony Tony'
                    WHERE rowid = '5'
    """)
    close_connection()

def delete_record():
    open_connection()
    cursor.execute("""DELETE FROM customers 
                    WHERE rowid = '2'
    """)
    close_connection()

def order_by():
    open_connection()
    items = cursor.execute("""SELECT rowid, * FROM customers 
                ORDER BY phone ASC
    """)
    for item in items:
        print(item)
    close_connection()

def and_or():
    open_connection()
    items = cursor.execute("""SELECT rowid, * FROM customers WHERE email LIKE '%gl.com' OR rowid = '5'
    """)
    for item in items:
        print(item)
    close_connection()

def limit():
    open_connection()
    items = cursor.execute("""SELECT rowid, * FROM customers 
                        WHERE email LIKE '%op.com' 
                        LIMIT 4
    """)
    for item in items:
        print(item)
    close_connection()

def delete_table():
    open_connection()
    cursor.execute("""DROP TABLE customers
    """)
    close_connection()

def main():
    # create_table()
    # insert_data(data)
    # insertmany_data(many_customers)
    # update_record()
    # delete_record()
    # order_by()
    # and_or()
    # limit()
    # search_by()
    # delete_table()
    
    show_rowid()


if __name__ == "__main__":
    main()
