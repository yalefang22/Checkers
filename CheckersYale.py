import tkinter as tk


class Checkers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.something = ""

    def create_widgets(self):
        self.red_sqr = 'red4'
        self.black_sqr = 'black'
        self.loadimage = tk.PhotoImage(file="Red_Circle.png")
        self.loadimage2 = tk.PhotoImage(file='greycircle.png')
        self.press = False
        self.row = 0
        self.column = 0

        for i in range(64):
            if self.column == 8:
                self.row += 1
                self.column = 0
            if self.row == 9:
                return 0

            if i < 24:
                if ((self.column % 2 == 0) and (self.row % 2 == 0)) or ((self.column % 2 != 0) and (self.row % 2 != 0)):
                    tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=self.row, column=self.column, sticky=tk.W)
                else:
                    tk.Button(self, image=self.loadimage, width=32, height=35, background=self.black_sqr).grid(row=self.row,
                                                                                                          column=self.column,
                                                                                                          sticky=tk.W)
            elif i >= 24 and i < 40:
                if ((self.column % 2 == 0) and (self.row % 2 == 0)) or ((self.column % 2 != 0) and (self.row % 2 != 0)):
                    tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=self.row, column=self.column, sticky=tk.W)
                else:
                    tk.Button(self, width=4, height=2, background=self.black_sqr).grid(row=self.row, column=self.column, sticky=tk.W)
            else:
                if ((self.column % 2 == 0) and (self.row % 2 == 0)) or ((self.column % 2 != 0) and (self.row % 2 != 0)):
                    tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=self.row, column=self.column, sticky=tk.W)
                else:
                    tk.Button(self, image=self.loadimage2, width=32, height=35, background=self.black_sqr,
                              ).grid(row=self.row,
                                                                                                           column=self.column,
                                                                                                           sticky=tk.W)

            self.column += 1







root = tk.Tk()
root.title("Checkers")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
