# Tried frames and Radio Buttons

from tkinter import *

root = Tk()
root.title('Now testing frames')

def update(value):
    my_label = Label(my_frm, text=value)
    my_label.pack() 

my_frm = LabelFrame(root, padx=30, pady=30)
my_frm.pack(padx=10, pady=10)

r = IntVar()

toppings = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in toppings:
    Radiobutton(my_frm, text=text, variable=pizza, value=topping).pack(anchor="w")

my_btn = Button(my_frm, text="Add Ingredient", command= lambda: update(pizza.get()))
my_btn.pack()

# Radiobutton(my_frm, text="Option 1", variable=r, value=1, command= lambda: update(r.get())).pack()
# Radiobutton(my_frm, text="Option 2", variable=r, value=2, command= lambda: update(r.get())).pack()

root.mainloop()