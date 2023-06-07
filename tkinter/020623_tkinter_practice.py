import tkinter as tk

window = tk.Tk()

# Calculate the desired width and height as a percentage of the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

width_percent = 0.3  # 30% of the screen width
height_percent = 0.8  # 80% of the screen height

window_width = int(screen_width * width_percent)
window_height = int(screen_height * height_percent)

# Set the window size. Make it responsive by commenting.
window.geometry(f"{window_width}x{window_height}")

# Get the coordinates to center the window on the screen
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 3

# Set the window position
window.geometry(f"+{x}+{y}")

frm_main = tk.Frame(
    bg = "#154360",
    borderwidth = 5,
)

frm_second = tk.Frame(
    master = frm_main,
    relief = "groove",
    borderwidth = 5,
    bg = "#154360",
    padx = 120,
)

# Creating the widgets
lbl_greeting = tk.Label(
    master = frm_second,
    text = "Getting used to it",
    bg = "#154360", # bg = background
    fg = "#A9CCE3", # fg = foreground
    width = "16",
    height = "1",
    )

btn_submit = tk.Button(
    master = frm_second,
    text = "Submit",
    fg = "blue",
    bg = "black",
    width = "7",
)

ent_data = tk.Entry(
    master = frm_second,
    fg = "#154360",
    bg = "#A9CCE3",
    width = "16",
    justify = "center",
)

btn_submit.configure(
    background="black"
)

# Packing widgets
lbl_greeting.pack()
ent_data.pack()
btn_submit.pack()

#Packing frame
frm_main.pack(
    fill = tk.BOTH,
    side = tk.TOP,
    expand = True,
    )
frm_second.pack()

# Main loop
window.mainloop()