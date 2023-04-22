import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result = tk.Entry(master, width=30, borderwidth=5)
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons
        button_1 = self.create_button("1", 1, 0)
        button_2 = self.create_button("2", 1, 1)
        button_3 = self.create_button("3", 1, 2)
        button_4 = self.create_button("4", 2, 0)
        button_5 = self.create_button("5", 2, 1)
        button_6 = self.create_button("6", 2, 2)
        button_7 = self.create_button("7", 3, 0)
        button_8 = self.create_button("8", 3, 1)
        button_9 = self.create_button("9", 3, 2)
        button_0 = self.create_button("0", 4, 1)

        button_add = self.create_button("+", 1, 3)
        button_subtract = self.create_button("-", 2, 3)
        button_multiply = self.create_button("*", 3, 3)
        button_divide = self.create_button("/", 4, 3)

        button_clear = tk.Button(master, text="Clear", padx=40, pady=20, command=self.clear)
        button_clear.grid(row=4, column=0)

        button_equal = tk.Button(master, text="=", padx=40, pady=20, command=self.calculate)
        button_equal.grid(row=4, column=2)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, padx=40, pady=20, command=lambda: self.append(text))
        button.grid(row=row, column=column)
        return button

    def append(self, value):
        current = self.result.get()
        self.result.delete(0, tk.END)
        self.result.insert(0, str(current) + str(value))

    def clear(self):
        self.result.delete(0, tk.END)

    def calculate(self):
        expression = self.result.get()
        try:
            result = eval(expression)
            self.result.delete(0, tk.END)
            self.result.insert(0, result)
        except:
            self.result.delete(0, tk.END)
            self.result.insert(0, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()