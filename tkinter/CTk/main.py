import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Trying CTk')
        self.geometry('400x600')
        self.grid_columnconfigure((0, 1), weight=1)

        self.btn = customtkinter.CTkButton(self, text='Button in CTk', command=self.button_pressed)
        self.btn.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="Checkbox I")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky='w')
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="Checkbox II")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='w')

    def button_pressed(self):
        print('You pressed')

app = App()
app.mainloop()