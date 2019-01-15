import tkinter as tk


class Checkers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self, width=32, height=35, background='black', command=self.movebutton
        ()).grid(row=2, column=1, sticky=tk.W)

    def movebutton(self):
        if self.button['bg'] == 'black':
            self.button = tk.Button(self, width=4, height=2, background='red4').grid(row=2, column=1, sticky=tk.W)


root = tk.Tk()
root.title("Checkers")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
