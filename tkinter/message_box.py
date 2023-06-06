from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Now trying message boxes')
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is a Popup", "Hey there!")
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text="Yes").pack()
    else:
        Label(root, text="No").pack()

Button(root, text="Popup", command = popup).pack()

root.mainloop()