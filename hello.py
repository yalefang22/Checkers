import tkinter as tk


class Checkers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.red_sqr = 'red4'
        self.black_sqr = 'black'
        self.redpiece = tk.PhotoImage(file="Red_Circle.png")
        self.blackpiece = tk.PhotoImage(file='greycircle.png')
        self.transparent = tk.PhotoImage(file='transparent.png')
        self.check = False
        self.piece = ""

        self.a1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=0, column=0, sticky=tk.W)
        self.a2 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr)
        self.a2.grid(row=0, column=1, sticky=tk.W)
        self.a3 = tk.Button(self, width=4, height=2, background=self.red_sqr)
        self.a3.grid(row=0, column=2, sticky=tk.W)
        self.a4 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movea4)
        self.a4.grid(row=0, column=3, sticky=tk.W)
        self.a5 = tk.Button(self, width=4, height=2, background=self.red_sqr)
        self.a5.grid(row=0, column=4, sticky=tk.W)
        self.a6 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movea6)
        self.a6.grid(row=0, column=5, sticky=tk.W)
        self.a7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=0, column=6, sticky=tk.W)
        self.a8 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movea8)
        self.a8.grid(row=0, column=7, sticky=tk.W)
        self.b1 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveb1)
        self.b1.grid(row=1, column=0, sticky=tk.W)
        self.b2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=1, sticky=tk.W)
        self.b3 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveb3)
        self.b3.grid(row=1, column=2, sticky=tk.W)
        self.b4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=3, sticky=tk.W)
        self.b5 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveb5)
        self.b5.grid(row=1, column=4, sticky=tk.W)
        self.b6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=5, sticky=tk.W)
        self.b7 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveb7)
        self.b7.grid(row=1, column=6, sticky=tk.W)
        self.b8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=7, sticky=tk.W)
        self.c1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=0, sticky=tk.W)
        self.c2 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movec2)
        self.c2.grid(row=2, column=1, sticky=tk.W)
        self.c3 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=2, sticky=tk.W)
        self.c4 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movec4)
        self.c4.grid(row=2, column=3, sticky=tk.W)
        self.c5 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=4, sticky=tk.W)
        self.c6 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movec6)
        self.c6.grid(row=2, column=5, sticky=tk.W)
        self.c7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=6, sticky=tk.W)
        self.c8 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movec8)
        self.c8.grid(row=2, column=7, sticky=tk.W)
        self.d1 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moved1)
        self.d1.grid(row=3, column=0, sticky=tk.W)
        self.d2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=3, column=1, sticky=tk.W)
        self.d3 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moved3)
        self.d3.grid(row=3, column=2, sticky=tk.W)
        self.d4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=3, column=3, sticky=tk.W)
        self.d5 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moved5)
        self.d5.grid(row=3, column=4, sticky=tk.W)
        self.d6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=3, column=5, sticky=tk.W)
        self.d7 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moved7)
        self.d7.grid(row=3, column=6, sticky=tk.W)
        self.d8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=3, column=7, sticky=tk.W)
        self.e1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=4, column=0, sticky=tk.W)
        self.e2 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movee2)
        self.e2.grid(row=4, column=1, sticky=tk.W)
        self.e3 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=4, column=2, sticky=tk.W)
        self.e4 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movee4)
        self.e4.grid(row=4, column=3, sticky=tk.W)
        self.e5 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=4, column=4, sticky=tk.W)
        self.e6 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movee6)
        self.e6.grid(row=4, column=5, sticky=tk.W)
        self.e7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=4, column=6, sticky=tk.W)
        self.e8 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movee7)
        self.e8.grid(row=4, column=7, sticky=tk.W)
        self.f1 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movef1)
        self.f1.grid(row=5, column=0, sticky=tk.W)
        self.f2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=1, sticky=tk.W)
        self.f3 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movef3)
        self.f3.grid(row=5, column=2, sticky=tk.W)
        self.f4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=3, sticky=tk.W)
        self.f5 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movef5)
        self.f5.grid(row=5, column=4, sticky=tk.W)
        self.f6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=5, sticky=tk.W)
        self.f7 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movef7)
        self.f7.grid(row=5, column=6, sticky=tk.W)
        self.f8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=7, sticky=tk.W)
        self.g1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=0, sticky=tk.W)
        self.g2 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveg2)
        self.g2.grid(row=6, column=1, sticky=tk.W)
        self.g3 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=2, sticky=tk.W)
        self.g4 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveg4)
        self.g4.grid(row=6, column=3, sticky=tk.W)
        self.g5 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=4, sticky=tk.W)
        self.g6 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveg6)
        self.g6.grid(row=6, column=5, sticky=tk.W)
        self.g7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=6, sticky=tk.W)
        self.g8 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveg8)
        self.g8.grid(row=6, column=7, sticky=tk.W)
        self.h1 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.moveh1)
        self.h1.grid(row=7, column=0, sticky=tk.W)
        self.h2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=1, sticky=tk.W)
        self.h3 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr)
        self.h3.grid(row=7, column=2, sticky=tk.W)
        self.h4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=3, sticky=tk.W)
        self.h5 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr)
        self.h5.grid(row=7, column=4, sticky=tk.W)
        self.h6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=5, sticky=tk.W)
        self.h7 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr)
        self.h7.grid(row=7, column=6, sticky=tk.W)
        self.h8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=7, sticky=tk.W)

    def movec2(self):
        if not self.check:
            if self.c2['image'] == 'pyimage1':
                self.c2.configure(image=self.transparent)
                self.piece = 'red'
            elif self.c2['image'] == 'pyimage2':
                self.c2.configure(image=self.transparent)
                self.piece = 'black'
            self.check = True
        elif self.check:
            if self.piece == 'red':
                self.c2.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.c2.configure(image=self.blackpiece)
            self.piece = ''
            self.check = False

    def moved1(self):
        if not self.check:
            if self.d1['image'] == 'pyimage1':
                self.d1.configure(image=self.transparent)
                self.piece = 'red'
            elif self.d1['image'] == 'pyimage2':
                self.d1.configure(image=self.transparent)
                self.piece = 'black'
            self.check = True
        elif self.check:
            if self.piece == 'red':
                self.d1.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.d1.configure(image=self.blackpiece)
            self.piece = ''
            self.check = False

    def movee2(self):
        if not self.check:
            if self.e2['image'] == 'pyimage1':
                self.e2.configure(image=self.transparent)
                self.piece = 'red'
            elif self.e2['image'] == 'pyimage2':
                self.e2.configure(image=self.transparent)
                self.piece = 'black'
            self.check = True
        elif self.check:
            if self.piece == 'red':
                self.e2.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.e2.configure(image=self.blackpiece)
            self.piece = ''
            self.check = False

    def movea4(self):
        if not self.check:
            if self.a4['image'] == 'pyimage1':
                self.a4.configure(image=self.transparent)
                self.piece = 'red'
            elif self.a4['image'] == 'pyimage2':
                self.a4.configure(image=self.transparent)
                self.piece = 'black'
            self.check = True
        elif self.check:
            if self.piece == 'red':
                self.a4.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.a4.configure(image=self.blackpiece)
            self.piece = ''
            self.check = False
    def movea6(self):
        if not self.check:
            if self.a6['image'] == 'pyimage1':
                self.a6.configure(image=self.transparent)
                self.piece = 'red'
            elif self.a6['image'] == 'pyimage2':
                self.a6.configure(image=self.transparent)
                self.piece = 'black'
            self.check = True
        elif self.check:
            if self.piece == 'red':
                self.a6.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.a6.configure(image=self.blackpiece)
            self.piece = ''
            self.check = False

root = tk.Tk()
root.title("Checkers")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
