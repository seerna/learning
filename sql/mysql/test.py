import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "root1234",
)

my_cursor = db.cursor()

def create_database():
    mycursor.execute("CREATE DATABASE testdatabase")

create_database()