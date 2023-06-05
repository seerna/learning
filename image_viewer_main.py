from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Another test page')

# Icon file not working. Maybe because of the filetype?
root.iconbitmap('images/icon.ico')

def back(image_number):
    global my_label
    global btn_back 
    global btn_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1], height=600, width=600)
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    btn_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        btn_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=1,column=0,columnspan=3)
    btn_back.grid(row=0,column=0)
    btn_forward.grid(row=0,column=2)
    status_bar = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status_bar.grid(row=2,column=0, columnspan=3, sticky=E + W)


def forward(image_number):
    global my_label
    global btn_back 
    global btn_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1], height=600, width=600)
    btn_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    btn_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        btn_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=1,column=0,columnspan=3)
    btn_back.grid(row=0,column=0)
    btn_forward.grid(row=0,column=2)
    status_bar = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status_bar.grid(row=2,column=0, columnspan=3, sticky=E + W)   


my_img1 = ImageTk.PhotoImage(Image.open("images/dog.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/img5.jpeg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]        

status_bar = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status_bar.grid(row=2,column=0, columnspan=3, sticky=E + W)

my_label = Label(root, image=image_list[0], height=600, width=600)
my_label.grid(row= 1, column=0, columnspan=3)

btn_quit = Button(root, text='Exit', command=root.quit)
btn_quit.grid(row=0,column=1)

btn_back = Button(root, text="<<", command=back)
btn_back.grid(row=0,column=0)                
                    
btn_forward = Button(root, text=">>", command=lambda: forward(2))
btn_forward.grid(row=0,column=2)

root.mainloop()