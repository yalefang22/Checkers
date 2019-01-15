from tkinter import *


class Checkers(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.loadimage = PhotoImage(file="Red_Circle.png")
        self.loadimage2 = PhotoImage(file="GreyCircle.png")
        self.button = Button(self, width=32, height=35, bg='black', command=self.movebutton, image=self.loadimage)
        self.button.grid(row=0, column=0, sticky=W)
        # self.button2 = Button(self, width=32, height=35, bg='red')
        # self.button2.grid(row=0, column=1, sticky=W)

    def movebutton(self):
        if self.button['bg'] == 'black':
            self.button.configure(bg='red4')
            # sets the image to none so that it disappears!
            self.loadimage = PhotoImage(None)
            self.button.configure(image=self.loadimage)
        elif self.button['bg'] == 'red4':
            self.button.configure(bg='black')
            self.button.configure(image=self.loadimage2)


root = Tk()
root.title("Checkers")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
