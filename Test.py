from tkinter import *


class Checkers(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self, width=4, height=2, bg='black', command=self.movebutton)
        self.button.grid(row=0, column=0, sticky=W)

    def movebutton(self):
        if self.button['bg'] == 'black':
            self.button.configure(bg='red4')
        elif self.button['bg'] == 'red4':
            self.button.configure(bg='black')


root = Tk()
root.title("Checkers")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
