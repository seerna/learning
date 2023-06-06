from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Time to play with windows')
# root.iconbitmap('')

def check():
    message = messagebox.askyesno("Confirmation","Open another window?")

    if message == 1:
        open_window()

def open_window():
    window = Toplevel()
    window.title('New window lol')
    # window.iconbitmap('')
    global image1
    image1 = ImageTk.PhotoImage(Image.open('images/img2.jpg'))
    image_to_show = Label(window, image=image1)
    image_to_show.grid(row=1, column=0)
    btn1 = Button(window,  text="Close", command= window.destroy)
    btn1.grid(row=0,column=0)

btn = Button(root, text='See here', command=check).pack()

root.mainloop()