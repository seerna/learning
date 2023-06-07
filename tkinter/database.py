from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('')
# root.iconbitmap('')
root.geometry('600x800')

def submit():
    # Create a database or connect to one
    connection = sqlite3.connect('address_book.db')
    # Creating a cursor
    cursor = connection.cursor()
    # Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state':state.get(),
                    'zipcode': zipcode.get(),
                })
    # Commit changes
    connection.commit()
    # Close connection
    connection.close()

    # Clearing entries
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    connection = sqlite3.connect('address_book.db')
    # Creating a cursor
    cursor = connection.cursor()

    # Query the database
    cursor.execute("SELECT * , oid FROM addresses")
    records = cursor.fetchall()
    
    # Loop thru results
    print_records = ""
    for record in records:
        print_records += str(record[6]) + "\t" + str(record[0]) + " " + str(record[1]) + "\n"

    query_lbl = Label(root, text=print_records)
    query_lbl.grid(row=8, column=0, columnspan=2)

    # Commit changes
    connection.commit()
    # Close connection
    connection.close()

def delete():
    connection = sqlite3.connect('address_book.db')
    cursor = connection.cursor()
    cursor.execute("DELETE from addresses WHERE oid= " + delete_ent.get())
    connection.commit()
    connection.close()

def edit():
    editor = Tk()
    editor.title('Entry editor')
    # root.iconbitmap('')
    editor.geometry('400x600')

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global edit_ent_editor

    # Creating textboxes for edition
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # Creating textbox labels for edition
    f_name_lbl_editor = Label(editor, text="First Name:")
    f_name_lbl_editor.grid(row=0, column=0)
    l_name_lbl_editor = Label(editor, text="Last Name:")
    l_name_lbl_editor.grid(row=1, column=0)
    address_lbl_editor = Label(editor, text="Address:")
    address_lbl_editor.grid(row=2, column=0)
    city_lbl_editor = Label(editor, text="City:")
    city_lbl_editor.grid(row=3, column=0)
    state_lbl_editor = Label(editor, text="State:")
    state_lbl_editor.grid(row=4, column=0)
    zipcode_lbl_editor = Label(editor, text="Zipcode:")
    zipcode_lbl_editor.grid(row=5, column=0)

    # Creating label, entry & button for edition
    edit_lbl_editor = Label(editor, text="Entry to edit:")
    edit_lbl_editor.grid(row=7, column=0)
    edit_ent_editor = Entry(editor, width=30)
    edit_ent_editor.grid(row=7, column=1, padx=20)
    edit_confirm_btn = Button(editor, text="Edit", command=update)
    edit_confirm_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
    # Button will be first as secutiry measure, oid will be the last set up

def update():
    connection = sqlite3.connect('address_book.db')
    cursor = connection.cursor()

    record_id = ``edit_ent_editor.get()

    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state':state_editor.get(),
            'zipcode': zipcode_editor.get(),

            'oid': record_id
        })

    connection.commit()
    connection.close()

# Create a database or connect to one
connection = sqlite3.connect('address_book.db')
# Creating a cursor
cursor = connection.cursor()
# Create table

try:
    cursor.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer    
        )""")
except:
    pass

# Commit changes
connection.commit()
# Close connection
connection.close()

# Creating textboxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Creating textbox labels
f_name_lbl = Label(root, text="First Name:")
f_name_lbl.grid(row=0, column=0)
l_name_lbl = Label(root, text="Last Name:")
l_name_lbl.grid(row=1, column=0)
address_lbl = Label(root, text="Address:")
address_lbl.grid(row=2, column=0)
city_lbl = Label(root, text="City:")
city_lbl.grid(row=3, column=0)
state_lbl = Label(root, text="State:")
state_lbl.grid(row=4, column=0)
zipcode_lbl = Label(root, text="Zipcode:")
zipcode_lbl.grid(row=5, column=0)

# Now creating a button to submit
submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Creating a query button to check on the data
query_btn = Button(root, text="Query the info", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=(10 , 30), ipadx=100)

# Creating delete structure
delete_lbl = Label(root, text="Entry to delete:")
delete_lbl.grid(row=9, column=0)

delete_ent = Entry(root, width=30)
delete_ent.grid(row=9, column=1, padx=20)

delete_btn = Button(root, text="Delete Entry", command=delete)
delete_btn.grid(row=10, column=0,columnspan=2, padx=10, pady=10, ipadx=100)

editor_btn = Button(root, text="Edit entry", command=edit)
editor_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

root.mainloop()