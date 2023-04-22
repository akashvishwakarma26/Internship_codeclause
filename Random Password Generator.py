import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Random Password Generator")

        
        self.password_label = tk.Label(master, text="Password Length:")
        self.password_label.grid(row=0, column=0)

        self.password_entry = tk.Entry(master)
        self.password_entry.grid(row=0, column=1, columnspan=2, padx=20, pady=20)

        
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        
        self.password_display = tk.Label(master, text="")
        self.password_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        
        length = int(self.password_entry.get())

        
        characters = string.ascii_letters + string.digits + string.punctuation

        
        password = ''.join(random.choice(characters) for i in range(length))

        
        self.password_display.config(text=password)

root = tk.Tk()
password_generator = PasswordGenerator(root)
root.mainloop()