import tkinter as tk
from temperature_converter import fahrenheit_to_celsius

def window_setup():
    window = tk.Tk()
    window.title("Temperature Converter")
    window.resizable(width=False, height=False)
    return window

def ent_lbl_creation(window):
    frm_entry = tk.Frame(master=window)
    ent_temperature = tk.Entry(master=frm_entry, width=10, justify="center")
    lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
    ent_temperature.grid(row=0, column=0, sticky="e")
    lbl_temp.grid(row=0, column=1, sticky="w")
    return frm_entry, ent_temperature

def btn_lbl_creation(window, ent_temperature):
    def convert_temperature():
        fahrenheit = ent_temperature.get()
        celsius = fahrenheit_to_celsius(fahrenheit)
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

    btn_convert = tk.Button(
        master=window,
        text="\N{RIGHTWARDS BLACK ARROW}",
        command=convert_temperature,
    )

    lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
    btn_convert.grid(row=0, column=1, pady=10)
    lbl_result.grid(row=0, column=2, padx=10)
    return btn_convert, lbl_result

def run_gui():
    window = window_setup()
    frm_entry, ent_temperature = ent_lbl_creation(window)
    btn_convert, lbl_result = btn_lbl_creation(window, ent_temperature)
    frm_entry.grid(row=0, column=0, padx=10)
    window.mainloop()