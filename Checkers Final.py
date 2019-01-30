import tkinter as tk


class Checkers(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.red_sqr = 'red4'
        self.black_sqr = 'black'
        self.redpiece = tk.PhotoImage(file="RedCircle.png")
        self.blackpiece = tk.PhotoImage(file='GreyCircle.png')
        self.transparent = tk.PhotoImage(file='transparent.png')
        self.purplepiece = tk.PhotoImage(file='PurpleButton.png')
        self.redking = tk.PhotoImage(file='RedKing.png')
        self.blackking = tk.PhotoImage(file='BlackKing.png')
        self.purpleking = tk.PhotoImage(file='PurpleKing.png')

        self.check = False
        self.piece = ""

        self.iskinga2 = False
        self.iskinga4 = False
        self.iskinga6 = False
        self.iskinga8 = False

        self.iskingb1 = False
        self.iskingb3 = False
        self.iskingb5 = False
        self.iskingb7 = False

        self.iskingc2 = False
        self.iskingc4 = False
        self.iskingc6 = False
        self.iskingc8 = False

        self.iskingd1 = False
        self.iskingd3 = False
        self.iskingd5 = False
        self.iskingd7 = False

        self.iskinge2 = False
        self.iskinge4 = False
        self.iskinge6= False
        self.iskinge8 = False

        self.iskingf1 = False
        self.iskingf3 = False
        self.iskingf5 = False
        self.iskingf7 = False

        self.iskingg2 = False
        self.iskingg4 = False
        self.iskingg6 = False
        self.iskingg8 = False

        self.iskingg1 = False
        self.iskingg3 = False
        self.iskingg5 = False
        self.iskingg7 = False

        self.ablea2 = False
        self.ablea4 = False
        self.ablea6 = False
        self.ablea8 = False

        self.ableb1 = False
        self.ableb3 = False
        self.ableb5 = False
        self.ableb7 = False

        self.ablec2 = False
        self.ablec4 = False
        self.ablec6 = False
        self.ablec8 = False

        self.abled1 = False
        self.abled3 = False
        self.abled5 = False
        self.abled7 = False

        self.ablee2 = False
        self.ablee4 = False
        self.ablee6 = False
        self.ablee8 = False

        self.ablef1 = False
        self.ablef3 = False
        self.ablef5 = False
        self.ablef7 = False

        self.ableg2 = False
        self.ableg4 = False
        self.ableg6 = False
        self.ableg8 = False

        self.ableh1 = False
        self.ableh3 = False
        self.ableh5 = False
        self.ableh7 = False


        self.a1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=0, column=0, sticky=tk.W)
        self.a2 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movea2)
        self.a2.grid(row=0, column=1, sticky=tk.W)
        self.a3 = tk.Button(self, width=4, height=2, background=self.red_sqr)
        self.a3.grid(row=0, column=2, sticky=tk.W)
        self.a4 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movea4)
        self.a4.grid(row=0, column=3, sticky=tk.W)
        self.a5 = tk.Button(self, width=4, height=2, background=self.red_sqr)
        self.a5.grid(row=0, column=4, sticky=tk.W)
        self.a6 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movea6)
        self.a6.grid(row=0, column=5, sticky=tk.W)
        self.a7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=0, column=6, sticky=tk.W)
        self.a8 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movea8)
        self.a8.grid(row=0, column=7, sticky=tk.W)
        self.b1 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.moveb1)
        self.b1.grid(row=1, column=0, sticky=tk.W)
        self.b2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=1, sticky=tk.W)
        self.b3 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.moveb3)
        self.b3.grid(row=1, column=2, sticky=tk.W)
        self.b4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=3, sticky=tk.W)
        self.b5 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.moveb5)
        self.b5.grid(row=1, column=4, sticky=tk.W)
        self.b6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=5, sticky=tk.W)
        self.b7 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.moveb7)
        self.b7.grid(row=1, column=6, sticky=tk.W)
        self.b8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=1, column=7, sticky=tk.W)
        self.c1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=0, sticky=tk.W)
        self.c2 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movec2)
        self.c2.grid(row=2, column=1, sticky=tk.W)
        self.c3 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=2, sticky=tk.W)
        self.c4 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movec4)
        self.c4.grid(row=2, column=3, sticky=tk.W)
        self.c5 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=4, sticky=tk.W)
        self.c6 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movec6)
        self.c6.grid(row=2, column=5, sticky=tk.W)
        self.c7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=2, column=6, sticky=tk.W)
        self.c8 = tk.Button(self, image=self.redpiece, width=32, height=35, background=self.black_sqr, command=self.movec8)
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
        self.e8 = tk.Button(self, image=self.transparent, width=32, height=35, background=self.black_sqr, command=self.movee8)
        self.e8.grid(row=4, column=7, sticky=tk.W)
        self.f1 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.movef1)
        self.f1.grid(row=5, column=0, sticky=tk.W)
        self.f2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=1, sticky=tk.W)
        self.f3 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.movef3)
        self.f3.grid(row=5, column=2, sticky=tk.W)
        self.f4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=3, sticky=tk.W)
        self.f5 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.movef5)
        self.f5.grid(row=5, column=4, sticky=tk.W)
        self.f6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=5, sticky=tk.W)
        self.f7 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.movef7)
        self.f7.grid(row=5, column=6, sticky=tk.W)
        self.f8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=5, column=7, sticky=tk.W)
        self.g1 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=0, sticky=tk.W)
        self.g2 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.moveg2)
        self.g2.grid(row=6, column=1, sticky=tk.W)
        self.g3 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=2, sticky=tk.W)
        self.g4 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.moveg4)
        self.g4.grid(row=6, column=3, sticky=tk.W)
        self.g5 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=4, sticky=tk.W)
        self.g6 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.moveg6)
        self.g6.grid(row=6, column=5, sticky=tk.W)
        self.g7 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=6, column=6, sticky=tk.W)
        self.g8 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.moveg8)
        self.g8.grid(row=6, column=7, sticky=tk.W)
        self.h1 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.moveh1)
        self.h1.grid(row=7, column=0, sticky=tk.W)
        self.h2 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=1, sticky=tk.W)
        self.h3 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.moveh3)
        self.h3.grid(row=7, column=2, sticky=tk.W)
        self.h4 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=3, sticky=tk.W)
        self.h5 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.moveh5)
        self.h5.grid(row=7, column=4, sticky=tk.W)
        self.h6 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=5, sticky=tk.W)
        self.h7 = tk.Button(self, image=self.blackpiece, width=32, height=35, background=self.black_sqr, command=self.moveh7)
        self.h7.grid(row=7, column=6, sticky=tk.W)
        self.h8 = tk.Button(self, width=4, height=2, background=self.red_sqr).grid(row=7, column=7, sticky=tk.W)


    def movea2(self):
        if not self.check:
            if self.a2['image'] == 'pyimage1':
                self.a2.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.a2['image'] == 'pyimage2':
                self.a2.configure(image=self.purplepiece)
                self.piece = 'black'
            elif self.a2['image'] == 'pyimage5':
                self.a2.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.a2['image'] == 'pyimage6':
                self.a2.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablea2 = True
            self.ableb1 = True
            self.ableb3 = True
        elif self.check and self.ablea2:
            if self.piece == 'redking':
                self.a2.configure(image=self.redking)
                if self.b1['image'] == 'pyimage7':
                    self.b1.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
            elif self.piece == 'black' or self.piece == 'blackking':
                self.a2.configure(image=self.blackking)
                if self.b1['image'] == 'pyimage4' or self.b1['image'] == 'pyimage7':
                    self.b1.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage4' or self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movea4(self):
        if not self.check:
            if self.a4['image'] == 'pyimage1':
                self.a4.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.a4['image'] == 'pyimage2':
                self.a4.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablea4 = True
            self.ableb3 = True
            self.ableb5 = True
        elif self.check and self.ablea4:
            if self.piece == 'red':
                self.a4.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.a4.configure(image=self.blackking)
                if self.b5['image'] == 'pyimage4':
                    self.b5.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage4':
                    self.b3.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movea6(self):
        if not self.check:
            if self.a6['image'] == 'pyimage1':
                self.a6.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.a6['image'] == 'pyimage2':
                self.a6.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablea6 = True
            self.ablea6 = True
            self.ableb5 = True
            self.ableb7 = True
        elif self.check and self.a6:
            if self.piece == 'red':
                self.a6.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.a6.configure(image=self.blackking)
                if self.b5['image'] == 'pyimage4':
                    self.b5.configure(image=self.transparent)
                elif self.b7['image'] == 'pyimage4':
                    self.b7.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movea8(self):
        if not self.check:
            if self.a8['image'] == 'pyimage1':
                self.a8.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.a8['image'] == 'pyimage2':
                self.a8.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablea8 = True
            self.ableb7 = True
        elif self.check and self.ablea8:
            if self.piece == 'red':
                self.a8.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.a8.configure(image=self.blackking)
                if self.b7['image'] == 'pyimage4':
                    self.b7.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveb1(self):
        if not self.check:
            if self.b1['image'] == 'pyimage1':
                self.b1.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.b1['image'] == 'pyimage2':
                self.b1.configure(image=self.purplepiece)
                self.piece = 'black'
            elif self.b1['image'] == 'pyimage5':
                self.b1.configure(image=self.purpleking)
                self.piece = 'redking'
            self.check = True
            self.ableb1 = True
            if self.piece == 'red' or self.isking(self.b1):
                self.ablec2 = True
            elif self.piece == 'black:' or self.isking(self.b1):
                self.ablea2 = True
        elif self.check and self.ableb1:
            if self.piece == 'red':
                self.b1.configure(image=self.redpiece)
                if self.a2['image'] == 'pyimage4':
                    self.a2.configure(image=self.transparent)
            elif self.piece == 'black':
                self.b1.configure(image=self.blackpiece)
                if self.c2['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveb3(self):
        if not self.check:
            if self.b3['image'] == 'pyimage1':
                self.b3.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.b3['image'] == 'pyimage2':
                self.b3.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableb3 = True
            if self.piece == 'red' or self.isking(self.b3):
                self.ablec2 = True
                self.ablec4 = True
            if self.piece == 'black' or self.isking(self.b3):
                self.ablea2 = True
                self.ablea4 = True
        elif self.check and self.ableb3:
            if self.piece == 'red':
                self.b3.configure(image=self.redpiece)
                if self.a2['image'] == 'pyimage4':
                    self.a2.configure(image=self.transparent)
                elif self.a4['image'] == 'pyimage4':
                    self.a4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.b3.configure(image=self.blackpiece)
                if self.c2['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()


    def moveb5(self):
        if not self.check:
            if self.b5['image'] == 'pyimage1':
                self.b5.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.b5['image'] == 'pyimage2':
                self.b5.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableb5 = True
            if self.piece == 'red' or self.isking(self.b5):
                self.ablec4 = True
                self.ablec6 = True
            if self.piece == 'black' or self.isking(self.b5):
                self.ablea4 = True
                self.ablea6 = True
        elif self.check and self.ableb5:
            if self.piece == 'red':
                self.b5.configure(image=self.redpiece)
                if self.a4['image'] == 'pyimage4':
                    self.a4.configure(image=self.transparent)
                elif self.a6['image'] == 'pyimage4':
                    self.a6.configure(image=self.transparent)
            elif self.piece == 'black':
                self.b5.configure(image=self.blackpiece)
                if self.c6['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveb7(self):
        if not self.check:
            if self.b7['image'] == 'pyimage1':
                self.b7.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.b7['image'] == 'pyimage2':
                self.b7.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableb7 = True
            if self.piece == 'red' or self.isking(self.b7):
                self.ablec6 = True
                self.ablec8 = True
            if self.piece == 'black' or self.isking(self.b7):
                self.ablea6 = True
                self.ablea8 = True
        elif self.check and self.ableb7:
            if self.piece == 'red':
                self.b7.configure(image=self.redpiece)
                if self.a8['image'] == 'pyimage4':
                    self.a8.configure(image=self.transparent)
                elif self.a6['image'] == 'pyimage4':
                    self.a6.configure(image=self.transparent)
            elif self.piece == 'black':
                self.b7.configure(image=self.blackpiece)
                if self.c8['image'] == 'pyimage4':
                    self.c8.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movec2(self):
        if not self.check:
            if self.c2['image'] == 'pyimage1':
                self.c2.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.c2['image'] == 'pyimage2':
                self.c2.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablec2 = True
            if self.piece == 'red' or self.isking(self.c2):
                self.abled1 = True
                self.abled3 = True
            if self.piece == 'black' or self.isking(self.c2):
                self.ableb1 = True
                self.ableb3 = True
        elif self.check and self.ablec2:
            if self.piece == 'red':
                self.c2.configure(image=self.redpiece)
                if self.b1['image'] == 'pyimage4':
                    self.b1.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage4':
                    self.b3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.c2.configure(image=self.blackpiece)
                if self.d1['image'] == 'pyimage4':
                    self.d1.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movec4(self):
        if not self.check:
            if self.c4['image'] == 'pyimage1':
                self.c4.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.c4['image'] == 'pyimage2':
                self.c4.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablec4 = True
            if self.piece == 'red' or self.isking(self.c4):
                self.abled3 = True
                self.abled5 = True
            if self.piece == 'black' or self.isking(self.c4):
                self.ableb3 = True
                self.ableb5 = True
        elif self.check and self.ablec4:
            if self.piece == 'red':
                self.c4.configure(image=self.redpiece)
                if self.b3['image'] == 'pyimage4':
                    self.b3.configure(image=self.transparent)
                elif self.b5['image'] == 'pyimage4':
                    self.b5.configure(image=self.transparent)
            elif self.piece == 'black':
                self.c4.configure(image=self.blackpiece)
                if self.d3['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
                elif self.d5['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movec6(self):
        if not self.check:
            if self.c6['image'] == 'pyimage1':
                self.c6.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.c6['image'] == 'pyimage2':
                self.c6.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablec6 = True
            if self.piece == 'red' or self.isking(self.c6):
                self.abled5 = True
                self.abled7 = True
            if self.piece == 'black' or self.isking(self.c6):
                self.ableb5 = True
                self.ableb7 = True
        elif self.check and self.ablec6:
            if self.piece == 'red':
                self.c6.configure(image=self.redpiece)
                if self.b5['image'] == 'pyimage4':
                    self.b5.configure(image=self.transparent)
                elif self.b7['image'] == 'pyimage4':
                    self.b7.configure(image=self.transparent)
            elif self.piece == 'black':
                self.c6.configure(image=self.blackpiece)
                if self.d5['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movec8(self):
        if not self.check:
            if self.c8['image'] == 'pyimage1':
                self.c8.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.c8['image'] == 'pyimage2':
                self.c8.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablec8 = True
            if self.piece == 'red' or self.isking(self.b3):
                self.abled7 = True
            if self.piece == 'black' or self.isking(self.b3):
                self.ableb7 = True
        elif self.check and self.ablec8:
            if self.piece == 'red':
                self.c8.configure(image=self.redpiece)
                if self.b7['image'] == 'pyimage4':
                    self.b7.configure(image=self.transparent)
            elif self.piece == 'black':
                self.c8.configure(image=self.blackpiece)
                if self.d7['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moved1(self):
        if not self.check:
            if self.d1['image'] == 'pyimage1':
                self.d1.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.d1['image'] == 'pyimage2':
                self.d1.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.abled1 = True
            if self.piece == 'red' or self.isking(self.d1):
                self.ablee2 = True
            if self.piece == 'black' or self.isking(self.d1):
                self.ablec2 = True
        elif self.check and self.abled1:
            if self.piece == 'red':
                self.d1.configure(image=self.redpiece)
                if self.c2['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
            elif self.piece == 'black':
                self.d1.configure(image=self.blackpiece)
                if self.e2['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moved3(self):
        if not self.check:
            if self.d3['image'] == 'pyimage1':
                self.d3.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.d3['image'] == 'pyimage2':
                self.d3.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.abled3 = True
            if self.piece == 'red' or self.isking(self.d3):
                self.ablee2 = True
                self.ablee4 = True
            if self.piece == 'black' or self.isking(self.d3):
                self.ablec2 = True
                self.ablec4 = True
        elif self.check and self.abled3:
            if self.piece == 'red':
                self.d3.configure(image=self.redpiece)
                if self.c2['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.d3.configure(image=self.blackpiece)
                if self.e2['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moved5(self):
        if not self.check:
            if self.d5['image'] == 'pyimage1':
                self.d5.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.d5['image'] == 'pyimage2':
                self.d5.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.abled5 = True
            if self.piece == 'red' or self.isking(self.d5):
                self.ablee4 = True
                self.ablee6 = True
            if self.piece == 'black' or self.isking(self.d5):
                self.ablec4 = True
                self.ablec6 = True
        elif self.check and self.abled5:
            if self.piece == 'red':
                self.d5.configure(image=self.redpiece)
                if self.c4['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
            elif self.piece == 'black':
                self.d5.configure(image=self.blackpiece)
                if self.e4['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moved7(self):
        if not self.check:
            if self.d7['image'] == 'pyimage1':
                self.d7.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.d7['image'] == 'pyimage2':
                self.d7.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.abled7 = True
            if self.piece == 'red' or self.isking(self.d7):
                self.ablee6 = True
                self.ablee8 = True
            if self.piece == 'black' or self.isking(self.d7):
                self.ablec6 = True
                self.ablec8 = True
        elif self.check and self.abled7:
            if self.piece == 'red':
                self.d7.configure(image=self.redpiece)
                if self.c8['image'] == 'pyimage4':
                    self.c8.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
            elif self.piece == 'black':
                self.d7.configure(image=self.blackpiece)
                if self.e8['image'] == 'pyimage4':
                    self.e8.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movee2(self):
        if not self.check:
            if self.e2['image'] == 'pyimage1':
                self.e2.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.e2['image'] == 'pyimage2':
                self.e2.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablee2 = True
            if self.piece == 'red' or self.isking(self.e2):
                self.ablef1 = True
                self.ablef3 = True
            if self.piece == 'black' or self.isking(self.e2):
                self.abled1 = True
                self.abled3 = True
        elif self.check and self.ablee2:
            if self.piece == 'red':
                self.e2.configure(image=self.redpiece)
                if self.d1['image'] == 'pyimage4':
                    self.d1.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.e2.configure(image=self.blackpiece)
                if self.f1['image'] == 'pyimage4':
                    self.f1.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movee4(self):
        if not self.check:
            if self.e4['image'] == 'pyimage1':
                self.e4.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.e4['image'] == 'pyimage2':
                self.e4.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablee4 = True
            if self.piece == 'red' or self.isking(self.e4):
                self.ablef3 = True
                self.ablef5 = True
            if self.piece == 'black' or self.isking(self.e4):
                self.abled3 = True
                self.abled5 = True
        elif self.check and self.ablee4:
            if self.piece == 'red':
                self.e4.configure(image=self.redpiece)
                if self.d5['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.e4.configure(image=self.blackpiece)
                if self.f5['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movee6(self):
        if not self.check:
            if self.e6['image'] == 'pyimage1':
                self.e6.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.e6['image'] == 'pyimage2':
                self.e6.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablee6 = True
            if self.piece == 'red' or self.isking(self.e6):
                self.ablef5 = True
                self.ablef7 = True
            if self.piece == 'black' or self.isking(self.e6):
                self.abled5 = True
                self.abled7 = True
        elif self.check and self.ablee6:
            if self.piece == 'red':
                self.e6.configure(image=self.redpiece)
                if self.d5['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
            elif self.piece == 'black':
                self.e6.configure(image=self.blackpiece)
                if self.f5['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movee8(self):
        if not self.check:
            if self.e8['image'] == 'pyimage1':
                self.e8.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.e8['image'] == 'pyimage2':
                self.e8.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablee8 = True
            if self.piece == 'red' or self.isking(self.e8):
                self.ablef7 = True
            if self.piece == 'black' or self.isking(self.e8):
                self.abled7 = True
        elif self.check and self.ablee8:
            if self.piece == 'red':
                self.e8.configure(image=self.redpiece)
                if self.d7['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
            elif self.piece == 'black':
                self.e8.configure(image=self.blackpiece)
                if self.f7['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movef1(self):
        if not self.check:
            if self.f1['image'] == 'pyimage1':
                self.f1.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.f1['image'] == 'pyimage2':
                self.f1.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablef1 = True
            if self.piece == 'red' or self.isking(self.f1):
                self.ableg2 = True
            if self.piece == 'black' or self.isking(self.f1):
                self.ablee2 = True
        elif self.check and self.ablef1:
            if self.piece == 'red':
                self.f1.configure(image=self.redpiece)
                if self.e2['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
            elif self.piece == 'black':
                self.f1.configure(image=self.blackpiece)
                if self.g2['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movef3(self):
        if not self.check:
            if self.f3['image'] == 'pyimage1':
                self.f3.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.f3['image'] == 'pyimage2':
                self.f3.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablef3 = True
            if self.piece == 'red' or self.isking(self.f3):
                self.ableg2 = True
                self.ableg4 = True
            if self.piece == 'black' or self.isking(self.f3):
                self.ablee2 = True
                self.ablee4 = True
        elif self.check and self.ablef3:
            if self.piece == 'red':
                self.f3.configure(image=self.redpiece)
                if self.e2['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.f3.configure(image=self.blackpiece)
                if self.g2['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movef5(self):
        if not self.check:
            if self.f5['image'] == 'pyimage1':
                self.f5.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.f5['image'] == 'pyimage2':
                self.f5.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablef5 = True
            if self.piece == 'red' or self.isking(self.f5):
                self.ableg4 = True
                self.ableg6 = True
            if self.piece == 'black' or self.isking(self.f5):
                self.ablee4 = True
                self.ablee6 = True
        elif self.check and self.ablef5:
            if self.piece == 'red':
                self.f5.configure(image=self.redpiece)
                if self.e6['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.f5.configure(image=self.blackpiece)
                if self.g6['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def movef7(self):
        if not self.check:
            if self.f7['image'] == 'pyimage1':
                self.f7.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.f7['image'] == 'pyimage2':
                self.f7.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ablef7 = True
            if self.piece == 'red' or self.isking(self.f7):
                self.ableg6 = True
                self.ableg8 = True
            if self.piece == 'black' or self.isking(self.f7):
                self.ablee6 = True
                self.ablee8 = True
        elif self.check and self.ablef7:
            if self.piece == 'red':
                self.f7.configure(image=self.redpiece)
                if self.e6['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                elif self.e8['image'] == 'pyimage4':
                    self.e8.configure(image=self.transparent)
            elif self.piece == 'black':
                self.f7.configure(image=self.blackpiece)
                if self.g6['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                elif self.g8['image'] == 'pyimage4':
                    self.g8.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveg2(self):
        if not self.check:
            if self.g2['image'] == 'pyimage1':
                self.g2.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.g2['image'] == 'pyimage2':
                self.g2.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableg2 = True
            if self.piece == 'red' or self.isking(self.g2):
                self.ableh1 = True
                self.ableh3 = True
            if self.piece == 'black' or self.isking(self.g2):
                self.ablef1 = True
                self.ablef3 = True
        elif self.check and self.ableg2:
            if self.piece == 'red':
                self.g2.configure(image=self.redpiece)
                if self.f1['image'] == 'pyimage4':
                    self.f1.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.g2.configure(image=self.blackpiece)
                if self.h1['image'] == 'pyimage4':
                    self.h1.configure(image=self.transparent)
                elif self.h3['image'] == 'pyimage4':
                    self.h3.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveg4(self):
        if not self.check:
            if self.g4['image'] == 'pyimage1':
                self.g4.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.g4['image'] == 'pyimage2':
                self.g4.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableg4 = True
            if self.piece == 'red' or self.isking(self.g4):
                self.ableh3 = True
                self.ableh5 = True
            if self.piece == 'black' or self.isking(self.g4):
                self.ablef3 = True
                self.ablef5 = True
        elif self.check and self.ableg4:
            if self.piece == 'red':
                self.g4.configure(image=self.redpiece)
                if self.f5['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.g4.configure(image=self.blackpiece)
                if self.h5['image'] == 'pyimage4':
                    self.h5.configure(image=self.transparent)
                elif self.h3['image'] == 'pyimage4':
                    self.h3.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveg6(self):
        if not self.check:
            if self.g6['image'] == 'pyimage1':
                self.g6.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.g6['image'] == 'pyimage2':
                self.g6.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableg6 = True
            if self.piece == 'red' or self.isking(self.g4):
                self.ableh5 = True
                self.ableh7 = True
            if self.piece == 'black' or self.isking(self.g6):
                self.ablef5 = True
                self.ablef7 = True
        elif self.check and self.ableg6:
            if self.piece == 'red':
                self.g6.configure(image=self.redpiece)
                if self.f5['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
            elif self.piece == 'black':
                self.g6.configure(image=self.blackpiece)
                if self.h5['image'] == 'pyimage4':
                    self.h5.configure(image=self.transparent)
                elif self.h7['image'] == 'pyimage4':
                    self.h7.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveg8(self):
        if not self.check:
            if self.g8['image'] == 'pyimage1':
                self.g8.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.g8['image'] == 'pyimage2':
                self.g8.configure(image=self.purplepiece)
                self.piece = 'black'
            elif self.g8['image'] == 'pyimage5':
                self.g8.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.g8['image'] == 'pyimage6':
                self.g8.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableg8 = True
            if self.piece == 'red' or self.isking(self.g8):
                self.ableh7 = True
            if self.piece == 'black' or self.isking(self.g8):
                self.ablef7 = True
        elif self.check and self.ableg8:
            if self.piece == 'red':
                self.g8.configure(image=self.redpiece)
            elif self.piece == 'black':
                self.g8.configure(image=self.blackpiece)
            elif self.piece == 'redking':
                self.g8.configure(image=self.redking)
            elif self.piece == 'blackking':
                self.g8.configure(image=self.blackking)
            if self.f7['image'] == 'pyimage4' or self.f7['image'] == 'pyimage7':
                self.f7.configure(image=self.transparent)
            elif self.h7['image'] == 'pyimage4' or self.h7['image'] == 'pyimage7':
                self.h7.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveh1(self):
        if not self.check:
            if self.h1['image'] == 'pyimage1':
                self.h1.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.h1['image'] == 'pyimage2':
                self.h1.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableh1 = True
            self.ableg2 = True
        elif self.check and self.ableh1:
            if self.piece == 'red':
                self.h1.configure(image=self.redking)
                if self.g2['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
            elif self.piece == 'black':
                self.h1.configure(image=self.blackpiece)
            self.piece = ''
            self.check = False
            self.clear()

    def moveh3(self):
        if not self.check:
            if self.h3['image'] == 'pyimage1':
                self.h3.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.h3['image'] == 'pyimage2':
                self.h3.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableh3 = True
            self.ableg2 = True
            self.ableg4 = True
        elif self.check and self.ableh3:
            if self.piece == 'red':
                self.h3.configure(image=self.redking)
                if self.g2['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.h3.configure(image=self.blackpiece)
            self.piece = ''
            self.check = False
            self.clear()

    def moveh5(self):
        if not self.check:
            if self.h5['image'] == 'pyimage1':
                self.h5.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.h5['image'] == 'pyimage2':
                self.h5.configure(image=self.purplepiece)
                self.piece = 'black'
            self.check = True
            self.ableh5 = True
            self.ableg4 = True
            self.ableg6 = True
        elif self.check and self.ableh5:
            if self.piece == 'red':
                self.h5.configure(image=self.redking)
                if self.g6['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.h5.configure(image=self.blackpiece)
            self.piece = ''
            self.check = False
            self.clear()

    def moveh7(self):
        if not self.check:
            if self.h7['image'] == 'pyimage5':
                self.h7.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.h7['image'] == 'pyimage2':
                self.h7.configure(image=self.purplepiece)
                self.piece = 'black'
            elif self.h7['image'] == 'pyimage6':
                self.h7.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableh7 = True
            self.ableg6 = True
            self.ableg8 = True
        elif self.check and self.ableh7:
            if self.piece == 'red' or self.piece == 'redking':
                self.h7.configure(image=self.redking)
                if self.g6['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                elif self.g8['image'] == 'pyimage4':
                    self.g8.configure(image=self.transparent)
            elif self.piece == 'black':
                self.h7.configure(image=self.blackpiece)
            elif self.piece == 'blackking':
                self.h7.configure(image=self.blackking)
            self.piece = ''
            self.check = False
            self.clear()

    def clear(self):
        self.ablea2 = False
        self.ablea4 = False
        self.ablea6 = False
        self.ablea8 = False

        self.ableb1 = False
        self.ableb3 = False
        self.ableb5 = False
        self.ableb7 = False

        self.ablec2 = False
        self.ablec4 = False
        self.ablec6 = False
        self.ablec8 = False

        self.abled1 = False
        self.abled3 = False
        self.abled5 = False
        self.abled7 = False

        self.ablee2 = False
        self.ablee4 = False
        self.ablee6 = False
        self.ablee8 = False

        self.ablef1 = False
        self.ablef3 = False
        self.ablef5 = False
        self.ablef7 = False

        self.ableg2 = False
        self.ableg4 = False
        self.ableg6 = False
        self.ableg8 = False

        self.ableh1 = False
        self.ableh3 = False
        self.ableh5 = False
        self.ableh7 = False

    def isking(self, piece):
        if self.piece == 'redking':
            return True
        elif piece['image'] == 'blackking':
            return True
        else:
            return False

root = tk.Tk()
root.title("Checkers")
root.geometry("600x400")
app = Checkers(root)
root.mainloop()
