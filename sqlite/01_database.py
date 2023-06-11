# sqlite datatypes are:
# NULL: something doesn't exists
# INTEGER: entire numbers
# REAL: decimal numbers
# TEXT: strings
# BLOB: stores as files are (images, mp3, files)

import sqlite3

database_name = 'customers.db'

# We first need to connect to a database
conn = sqlite3.connect(database_name)

# You can also connect to a database in memory
# conn = sqlite3.connect(':memory:')

# We create cursors to take actions over databases
cursor = conn.cursor()

many_customers = [
                    ('Luffy', 'Monkey D.', 'md.luffy@op.com', '3158208703'),
                    ('Zoro', 'Roronoa', 'rzoro@op.com', '3124492894'),
                    ('Tony', 'Chopper', 'tchopper@op.com', '3002344892'),
                ]

# Create a table
def create_table(cursor):
    cursor.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text,
    phone int
    )
    """)
    # commiting our command
    conn.commit()
    # close our connection
    conn.close()

def insert_data(cursor):
    cursor.execute("INSERT INTO customers VALUES ('Ve', 'Nus', 'vnus@wgovt.com', '3124537864')")
    print('Data added')
    conn.commit()
    conn.close()

def insertmany_data(cursor, many_customers):
    cursor.executemany("INSERT INTO customers VALUES (?,?,?,?)", many_customers)
    print('Many Data added')
    conn.commit()
    conn.close()

def query_data(cursor):
    cursor.execute("SELECT * FROM customers")
    # print(cursor.fetchone()[0])
    # print(cursor.fetchmany(2))
    items = cursor.fetchall()
    print('NAME\t' + 'Email')
    print("---\t" + '---')
    for item in items:
        print(item[0] + "\t" + item[2])
    

# create_table(cursor) # Commented as the table is already created
# insert_data(cursor)
# insertmany_data(cursor, many_customers)
query_data(cursor)