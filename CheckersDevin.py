import tkinter as tk


class Checkers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        red_sqr = 'red4'
        black_sqr = 'black'
        self.loadimage = tk.PhotoImage(file="Red_Circle.png")
        self.loadimage2 = tk.PhotoImage(file="GreyCircle.png")

        row = 0
        column = 0

        for i in range(64):
            if column == 8:
                row += 1
                column = 0
            if row == 9:
                return 0

            if i < 24:
                if ((column % 2 == 0) and (row % 2 == 0)) or ((column % 2 != 0) and (row % 2 != 0)):
                    tk.Button(self, width=4, height=2, background=red_sqr).grid(row=row, column=column, sticky=tk.W)
                else:
                    tk.Button(self, image=self.loadimage, width=32, height=35, background=black_sqr).grid(row=row,
                                                                                                          column=column,
                                                                                                          sticky=tk.W)
            elif i >= 24 and i < 40:
                if ((column % 2 == 0) and (row % 2 == 0)) or ((column % 2 != 0) and (row % 2 != 0)):
                    tk.Button(self, width=4, height=2, background=red_sqr).grid(row=row, column=column, sticky=tk.W)
                else:
                    tk.Button(self, width=4, height=2, background=black_sqr).grid(row=row, column=column, sticky=tk.W)
            else:
                if ((column % 2 == 0) and (row % 2 == 0)) or ((column % 2 != 0) and (row % 2 != 0)):
                    tk.Button(self, width=4, height=2, background=red_sqr).grid(row=row, column=column, sticky=tk.W)
                else:
                    tk.Button(self, image=self.loadimage2, width=32, height=35, background=black_sqr).grid(row=row,
                                                                                                          column=column,
                                                                                                          sticky=tk.W)

            column += 1


root = tk.Tk()
root.title("Mad Libs")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()

