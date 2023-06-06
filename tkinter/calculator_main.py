from tkinter import *

root = Tk()
root.title("Simple Calculator")

def ent_creation():
    myEntry = Entry(
        root,
        width= 35,
        borderwidth= 5,
    )
    myEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    return myEntry

def btn_creation(myEntry):
    # operation variables goes for the type of ops. 0 = clear, 1 = sum, 2 = substraction, 3 = multiply, 4 = division
    global operation
    operation = 0

    def button_click(number):
        current = myEntry.get()
        myEntry.delete(0, END)
        myEntry.insert(0, str(current) + str(number))

    def button_clear():
        global operation
        operation = 0
        myEntry.delete(0, END)

    def button_add():
        global operation
        operation = 1
        first_number = myEntry.get()
        global f_num
        f_num = float(first_number)
        myEntry.delete(0, END)

    def button_sub():
        global operation
        operation = 2
        first_number = myEntry.get()
        global f_num
        f_num = float(first_number)
        myEntry.delete(0, END)

    def button_mul():
        global operation
        operation = 3
        first_number = myEntry.get()
        global f_num
        f_num = float(first_number)
        myEntry.delete(0, END)

    def button_div():
        global operation
        operation = 4
        first_number = myEntry.get()
        global f_num
        f_num = float(first_number)
        myEntry.delete(0, END)    

    def button_equal():
        second_number = myEntry.get()
        result = 0
        
        if operation == 0:
            button_clear()
        elif operation == 1:
            result = f_num + float(second_number)
            myEntry.delete(0, END)
            myEntry.insert(0, result)
        elif operation == 2:
            result = f_num - float(second_number)
            myEntry.delete(0, END)
            myEntry.insert(0, result)
        elif operation == 3:
            result = f_num * float(second_number)
            myEntry.delete(0, END)
            myEntry.insert(0, result)
        elif operation == 4:
            result = f_num / int(second_number)
            myEntry.delete(0, END)
            myEntry.insert(0, result)   
    
    # Creating the buttons
    btn_1 = Button(root,text="1",padx=40,pady=20,command= lambda: button_click(1))
    btn_2 = Button(root,text="2",padx=40,pady=20,command= lambda: button_click(2))
    btn_3 = Button(root,text="3",padx=40,pady=20,command= lambda: button_click(3))
    btn_4 = Button(root,text="4",padx=40,pady=20,command= lambda: button_click(4))
    btn_5 = Button(root,text="5",padx=40,pady=20,command= lambda: button_click(5))
    btn_6 = Button(root,text="6",padx=40,pady=20,command= lambda: button_click(6))
    btn_7 = Button(root,text="7",padx=40,pady=20,command= lambda: button_click(7))
    btn_8 = Button(root,text="8",padx=40,pady=20,command= lambda: button_click(8))
    btn_9 = Button(root,text="9",padx=40,pady=20,command= lambda: button_click(9))
    btn_0 = Button(root,text="0",padx=40,pady=20,command= lambda: button_click(0))

    btn_add = Button(root,text="+",padx=39,pady=20,command= button_add)
    btn_sub = Button(root,text="-",padx=39,pady=20,command= button_sub)
    btn_mul = Button(root,text="*",padx=39,pady=20,command= button_mul)
    btn_div = Button(root,text="/",padx=39,pady=20,command= button_div)
    
    
    btn_equal = Button(root,text="=",padx=91,pady=20,command= button_equal)
    btn_clear = Button(root,text="Clear",padx=71,pady=20,command= button_clear)

    # Setting buttons on screen
    btn_1.grid(row=3,column=0)
    btn_2.grid(row=3,column=1)
    btn_3.grid(row=3,column=2)

    btn_4.grid(row=2,column=0)
    btn_5.grid(row=2,column=1)
    btn_6.grid(row=2,column=2)

    btn_7.grid(row=1,column=0)
    btn_8.grid(row=1,column=1)
    btn_9.grid(row=1,column=2)

    btn_0.grid(row=4,column=0)

    btn_add.grid(row=4,column=1)

    btn_sub.grid(row=4,column=2)
    btn_mul.grid(row=6,column=0)
    btn_div.grid(row=5,column=0)

    btn_clear.grid(row=5,column=1, columnspan=2)
    btn_equal.grid(row=6,column=1, columnspan=2)

entry = ent_creation()
btn_creation(entry)

root.mainloop()