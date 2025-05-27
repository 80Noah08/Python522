import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def calculate(self):
        try:
            first_value = float(self.firstNumberEntry.get())
            second_value = float(self.secondNumberEntry.get())
            result = first_value + second_value
            self.resultLable.config(text=str(result), bg="green", fg="white")
        except ValueError:
            self.resultLable.config(text="Not number/s.", bg="red", fg="black")

    def create_widgets(self):
        self.firstNumberEntry = tk.Entry()
        self.plusSing = tk.Label(text="+")
        self.secondNumberEntry = tk.Entry()
        self.equalSing = tk.Label(text="=")
        self.resultLable = tk.Label(text="Result...", bg="green", fg="white")
        self.calculateButton = tk.Button(text="Calculate", command=self.calculate)



    # place widgets
        self.firstNumberEntry.pack(side="left")
        self.plusSing.pack(side="left")
        self.secondNumberEntry.pack(side="left")
        self.equalSing.pack(side="left")
        self.resultLable.pack(side="left")
        self.calculateButton.pack(side="left")


# create the application
app = Application()
app.master.title("Sumator")
app.master.minsize(width=100, height=50)

# start the program
app.mainloop()
