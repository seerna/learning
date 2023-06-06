from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')
# root.iconbitmap('')
root.geometry("400x400")

a_slider_vertical = Scale(
    root,
    from_=0, to=1080,
)
a_slider_vertical.pack(anchor="e") #Sliders should be packed on it's own line

a_slider_horizontal = Scale(
    root,
    from_=0, to=2540,
    orient="horizontal"
)
a_slider_horizontal.pack(anchor="s")

def slide():
    global a_fking_label
    a_fking_label = Label(
        root,
        text=str(a_slider_horizontal.get()) + "x" + str(a_slider_vertical.get())).pack()
    root.geometry(str(a_slider_horizontal.get()) + "x" + str(a_slider_vertical.get()))

a_btn = Button(root, text="Srsly", command=slide).pack()

root.mainloop()