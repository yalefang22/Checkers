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
        self.transparent = tk.PhotoImage(file='Transparent.png')
        self.purplepiece = tk.PhotoImage(file='PurpleButton.png')
        self.redking = tk.PhotoImage(file='RedKing.png')
        self.blackking = tk.PhotoImage(file='BlackKing.png')
        self.purpleking = tk.PhotoImage(file='PurpleKing.png')


        self.check = False
        self.piece = ""

        self.isking = False

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
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.b3['image'] != 'pyimage3':
                    self.ableb3 = False
                else:
                    self.ableb3 = True
                if self.b3['image'] == 'pyimage2' or self.c4['image'] == 'pyimage3':
                    self.ablec4 = True
                else:
                    self.ablec4 = False
                if self.b1['image'] != 'pyimage3':
                    self.ableb1 = False
                else:
                    self.ableb1 = True
        elif self.check and self.ablea2:
            if self.piece == 'red':
                self.a2.configure(image=self.redpiece)
            elif self.piece == 'black' or self.piece == 'blackking':
                self.a2.configure(image=self.blackking)
                if self.b1['image'] == 'pyimage4' or self.b1['image'] == 'pyimage7':
                    self.b1.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage4' or self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
                elif (self.b3['image'] == 'pyimage1' or self.b3['image'] == 'pyimage5') and (self.c4['image'] == 'pyimage4' or self.c4['image'] == 'pyimage7'):
                    self.b3.configure(image=self.transparent)
                    self.c4.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.a2.configure(image=self.redking)
                if self.b1['image'] == 'pyimage4' or self.b1['image'] == 'pyimage7':
                    self.b1.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage4' or self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
                elif (self.b3['image'] == 'pyimage2' or self.b3['image'] == 'pyimage6') and (self.c4['image'] == 'pyimage4' or self.c4['image'] == 'pyimage7'):
                    self.b3.configure(image=self.transparent)
                    self.c4.configure(image=self.transparent)
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
            elif self.a4['image'] == 'pyimage5':
                self.a4.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.a4['image'] == 'pyimage6':
                self.a4.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablea4 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.b3['image'] != 'pyimage3':
                    self.ableb3 = False
                else:
                    self.ableb3 = True
                if self.b3['image'] == 'pyimage2' or self.c2['image'] == 'pyimage3':
                    self.ablec2 = True
                else:
                    self.ablec2 = False
                if self.b5['image'] != 'pyimage3':
                    self.ableb5 = False
                else:
                    self.ableb5 = True
                if self.b5['image'] == 'pyimage2' or self.c6['image'] == 'pyimage3':
                    self.ablec6 = True
                else:
                    self.ablec6 = False
        elif self.check and self.ablea4:
            if self.piece == 'red':
                self.a4.configure(image=self.redpiece)
            elif self.piece == 'black' or self.piece == 'blackking':
                self.a4.configure(image=self.blackking)
                if self.b5['image'] == 'pyimage4' or self.b5['image'] == 'pyimage7':
                    self.b5.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage4' or self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
                elif (self.b3['image'] == 'pyimage1' or self.b3['image'] == 'pyimage5') and (self.c2['image'] == 'pyimage4' or self.c2['image'] == 'pyimage7'):
                    self.b3.configure(image=self.transparent)
                    self.c2.configure(image=self.transparent)
                elif (self.b5['image'] == 'pyimage1' or self.b5['image'] == 'pyimage5') and (self.c6['image'] == 'pyimage4' or self.c6['image'] == 'pyimage7'):
                    self.b5.configure(image=self.transparent)
                    self.c6.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.a4.configure(image=self.redking)
                if self.b5['image'] == 'pyimage4' or self.b5['image'] == 'pyimage7':
                    self.b5.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage4' or self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
                elif (self.b3['image'] == 'pyimage2' or self.b3['image'] == 'pyimage6') and (self.c2['image'] == 'pyimage4' or self.c2['image'] == 'pyimage7'):
                    self.b3.configure(image=self.transparent)
                    self.c2.configure(image=self.transparent)
                elif (self.b5['image'] == 'pyimage2' or self.b5['image'] == 'pyimage6') and (self.c6['image'] == 'pyimage4' or self.c6['image'] == 'pyimage7'):
                    self.b5.configure(image=self.transparent)
                    self.c6.configure(image=self.transparent)
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
            elif self.a6['image'] == 'pyimage5':
                self.a6.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.a6['image'] == 'pyimage6':
                self.a6.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablea6 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.b7['image'] != 'pyimage3':
                    self.ableb7 = False
                else:
                    self.ableb7 = True
                if self.b7['image'] == 'pyimage2' or self.c8['image'] == 'pyimage3':
                    self.ablec8 = True
                else:
                    self.ablec8 = False
                if self.b5['image'] != 'pyimage3':
                    self.ableb5 = False
                else:
                    self.ableb5 = True
                if self.b5['image'] == 'pyimage2' or self.c4['image'] == 'pyimage3':
                    self.ablec4 = True
                else:
                    self.ablec4 = False
        elif self.check and self.ablea6:
            if self.piece == 'red':
                self.a6.configure(image=self.redpiece)
            elif self.piece == 'black' or self.piece == 'blackking':
                self.a6.configure(image=self.blackking)
                if self.b5['image'] == 'pyimage4' or self.b5['image'] == 'pyimage7':
                    self.b5.configure(image=self.transparent)
                elif self.b7['image'] == 'pyimage4' or self.b7['image'] == 'pyimage7':
                    self.b7.configure(image=self.transparent)
                elif (self.b7['image'] == 'pyimage1' or self.b7['image'] == 'pyimage5') and (self.c8['image'] == 'pyimage4' or self.c8['image'] == 'pyimage7'):
                    self.b7.configure(image=self.transparent)
                    self.c8.configure(image=self.transparent)
                elif (self.b5['image'] == 'pyimage1' or self.b5['image'] == 'pyimage5') and (self.c4['image'] == 'pyimage4' or self.c4['image'] == 'pyimage7'):
                    self.b5.configure(image=self.transparent)
                    self.c4.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.a6.configure(image=self.redking)
                if self.b5['image'] == 'pyimage4' or self.b5['image'] == 'pyimage7':
                    self.b5.configure(image=self.transparent)
                elif self.b7['image'] == 'pyimage4' or self.b7['image'] == 'pyimage7':
                    self.b7.configure(image=self.transparent)
                elif (self.b7['image'] == 'pyimage2' or self.b7['image'] == 'pyimage6') and (
                        self.c8['image'] == 'pyimage4' or self.c8['image'] == 'pyimage7'):
                    self.b7.configure(image=self.transparent)
                    self.c8.configure(image=self.transparent)
                elif (self.b5['image'] == 'pyimage2' or self.b5['image'] == 'pyimage6') and (
                        self.c4['image'] == 'pyimage4' or self.c4['image'] == 'pyimage7'):
                    self.b5.configure(image=self.transparent)
                    self.c4.configure(image=self.transparent)
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
            elif self.a8['image'] == 'pyimage5':
                self.a8.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.a8['image'] == 'pyimage6':
                self.a8.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablea8 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.b7['image'] != 'pyimage3':
                    self.ableb7 = False
                else:
                    self.ableb7 = True
                if self.b7['image'] == 'pyimage2' or self.c6['image'] == 'pyimage3':
                    self.ablec6 = True
                else:
                    self.ablec6 = False
        elif self.check and self.ablea8:
            if self.piece == 'red':
                self.a8.configure(image=self.redpiece)
            elif self.piece == 'black' or self.piece == 'blackking':
                self.a8.configure(image=self.blackking)
                if self.b7['image'] == 'pyimage4' or self.b7['image'] == 'pyimage7':
                    self.b7.configure(image=self.transparent)
                elif (self.b7['image'] == 'pyimage1' or self.b7['image'] == 'pyimage5') and (self.c6['image'] == 'pyimage4' or self.c6['image'] == 'pyimage7'):
                    self.b7.configure(image=self.transparent)
                    self.c6.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.a8.configure(image=self.redking)
                if self.b7['image'] == 'pyimage4' or self.b7['image'] == 'pyimage7':
                    self.b7.configure(image=self.transparent)
                elif (self.b7['image'] == 'pyimage2' or self.b7['image'] == 'pyimage6') and (self.c6['image'] == 'pyimage4' or self.c6['image'] == 'pyimage7'):
                    self.b7.configure(image=self.transparent)
                    self.c6.configure(image=self.transparent)
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
            elif self.b1['image'] == 'pyimage6':
                self.b1.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableb1 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.c2['image'] != 'pyimage3':
                    self.ablec2 = False
                else:
                    self.ablec2 = True
                if self.c2['image'] == 'pyimage2' or self.d3['image'] == 'pyimage3':
                    self.abled3 = True
                else:
                    self.abled3 = False
            if self.piece == 'black' or self.piece == 'redking'or self.piece == 'blackking':
                if self.a2['image'] != 'pyimage3':
                    self.ablea2 = False
                else:
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
                elif self.c2['image'] == 'pyimage1' and self.d3['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.b1.configure(image=self.redking)
                if self.c2['image'] == 'pyimage7':
                    self.c2.configure(image=self.transparent)
                elif self.a2['image'] == 'pyimage7':
                    self.a2.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.b1.configure(image=self.blackking)
                if self.c2['image'] == 'pyimage7':
                    self.c2.configure(image=self.transparent)
                elif self.a2['image'] == 'pyimage7':
                    self.a2.configure(image=self.transparent)
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
            elif self.b3['image'] == 'pyimage5':
                self.b3.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.b3['image'] == 'pyimage6':
                self.b3.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableb3 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.c2['image'] != 'pyimage3':
                    self.ablec2 = False
                else:
                    self.ablec2 = True
                if self.c2['image'] == 'pyimage2' or self.d1['image'] == 'pyimage3':
                    self.abled1 = True
                else:
                    self.abled1 = False
                if self.c4['image'] != 'pyimage3':
                    self.ablec4 = False
                else:
                    self.ablec4 = True
                if self.c4['image'] == 'pyimage2' or self.d5['image'] == 'pyimage3':
                    self.abled5 = True
                else:
                    self.abled5 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.a2['image'] != 'pyimage3':
                    self.ablea2 = False
                else:
                    self.ablea2 = True
                if self.a4['image'] != 'pyimage3':
                    self.ablea4 = False
                else:
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
                elif self.c2['image'] == 'pyimage1' and self.d1['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
                    self.d1.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage1' and self.d5['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
                    self.d5.configure(image=self.transparent)
            elif self.piece == 'redking':
                    self.b3.configure(image=self.redking)
                    if self.c2['image'] == 'pyimage7':
                        self.c2.configure(image=self.transparent)
                    elif self.a2['image'] == 'pyimage7':
                        self.a2.configure(image=self.transparent)
                    if self.c4['image'] == 'pyimage7':
                        self.c4.configure(image=self.transparent)
                    elif self.a4['image'] == 'pyimage7':
                        self.a4.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.b3.configure(image=self.blackking)
                if self.c2['image'] == 'pyimage7':
                    self.c2.configure(image=self.transparent)
                elif self.a2['image'] == 'pyimage7':
                    self.a2.configure(image=self.transparent)
                if self.c4['image'] == 'pyimage7':
                    self.c4.configure(image=self.transparent)
                elif self.a4['image'] == 'pyimage7':
                    self.a4.configure(image=self.transparent)
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
            elif self.b5['image'] == 'pyimage5':
                self.b5.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.b5['image'] == 'pyimage6':
                self.b5.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableb5 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.c6['image'] != 'pyimage3':
                    self.ablec6 = False
                else:
                    self.ablec6 = True
                if self.c6['image'] == 'pyimage2' or self.d7['image'] == 'pyimage3':
                    self.abled7 = True
                else:
                    self.abled7 = False
                if self.c4['image'] != 'pyimage3':
                    self.ablec4 = False
                else:
                    self.ablec4 = True
                if self.c4['image'] == 'pyimage2' or self.d3['image'] == 'pyimage3':
                    self.abled3 = True
                else:
                    self.abled3 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.a6['image'] != 'pyimage3':
                    self.ablea6 = False
                else:
                    self.ablea6 = True
                if self.a4['image'] != 'pyimage3':
                    self.ablea4 = False
                else:
                    self.ablea4 = True
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
                elif self.c6['image'] == 'pyimage1' and self.d7['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
                    self.d7.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage1' and self.d3['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.b5.configure(image=self.redking)
                if self.c6['image'] == 'pyimage7':
                    self.c6.configure(image=self.transparent)
                elif self.a6['image'] == 'pyimage7':
                    self.a6.configure(image=self.transparent)
                if self.c4['image'] == 'pyimage7':
                    self.c4.configure(image=self.transparent)
                elif self.a4['image'] == 'pyimage7':
                    self.a4.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.b5.configure(image=self.blackking)
                if self.c6['image'] == 'pyimage7':
                    self.c6.configure(image=self.transparent)
                elif self.a6['image'] == 'pyimage7':
                    self.a6.configure(image=self.transparent)
                if self.c4['image'] == 'pyimage7':
                    self.c4.configure(image=self.transparent)
                elif self.a4['image'] == 'pyimage7':
                    self.a4.configure(image=self.transparent)
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
            elif self.b7['image'] == 'pyimage5':
                self.b7.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.b7['image'] == 'pyimage6':
                self.b7.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableb7 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.c6['image'] != 'pyimage3':
                    self.ablec6 = False
                else:
                    self.ablec6 = True
                if self.c6['image'] == 'pyimage2' or self.d5['image'] == 'pyimage3':
                    self.abled5 = True
                else:
                    self.abled5 = False
                if self.c8['image'] != 'pyimage3':
                    self.ablec8 = False
                else:
                    self.ablec8 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.a6['image'] != 'pyimage3':
                    self.ablea6 = False
                else:
                    self.ablea6 = True
                if self.a8['image'] != 'pyimage3':
                    self.ablea8 = False
                else:
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
                elif self.c6['image'] == 'pyimage1' and self.d5['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
                    self.d5.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.b7.configure(image=self.redking)
                if self.c6['image'] == 'pyimage7':
                    self.c6.configure(image=self.transparent)
                elif self.a6['image'] == 'pyimage7':
                    self.a6.configure(image=self.transparent)
                if self.c8['image'] == 'pyimage7':
                    self.c8.configure(image=self.transparent)
                elif self.a8['image'] == 'pyimage7':
                    self.a8.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.b7.configure(image=self.blackking)
                if self.c6['image'] == 'pyimage7':
                    self.c6.configure(image=self.transparent)
                elif self.a6['image'] == 'pyimage7':
                    self.a6.configure(image=self.transparent)
                if self.c8['image'] == 'pyimage7':
                    self.c8.configure(image=self.transparent)
                elif self.a8['image'] == 'pyimage7':
                    self.a8.configure(image=self.transparent)
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
            elif self.c2['image'] == 'pyimage5':
                self.c2.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.c2['image'] == 'pyimage6':
                self.c2.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablec2 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.d3['image'] != 'pyimage3':
                    self.abled3 = False
                else:
                    self.abled3 = True
                if self.d3['image'] == 'pyimage2' or self.e4['image'] == 'pyimage3':
                    self.ablee4 = True
                else:
                    self.ablee2 = False
                if self.d1['image'] != 'pyimage3':
                    self.abled1 = False
                else:
                    self.abled1 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.b3['image'] != 'pyimage3':
                    self.ableb3 = False
                else:
                    self.ableb3 = True
                if self.b3['image'] == 'pyimage2' or self.a4['image'] == 'pyimage3':
                    self.ablea4 = True
                else:
                    self.ablea4 = False
                if self.b1['image'] != 'pyimage3':
                    self.ableb1 = False
                else:
                    self.ableb1 = True
        elif self.check and self.ablec2:
            if self.piece == 'red':
                self.c2.configure(image=self.redpiece)
                if self.b1['image'] == 'pyimage4':
                    self.b1.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage4':
                    self.b3.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage2' and self.a4['image'] == 'pyimage4':
                    self.a4.configure(image=self.transparent)
                    self.b3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.c2.configure(image=self.blackpiece)
                if self.d1['image'] == 'pyimage4':
                    self.d1.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage1' and self.e4['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
                    self.e4.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.c2.configure(image=self.redking)
                if self.b1['image'] == 'pyimage7':
                    self.b1.configure(image=self.transparent)
                elif self.d1['image'] == 'pyimage7':
                    self.d1.configure(image=self.transparent)
                if self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage7':
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.c2.configure(image=self.blackking)
                if self.b1['image'] == 'pyimage7':
                    self.b1.configure(image=self.transparent)
                elif self.d1['image'] == 'pyimage7':
                    self.d1.configure(image=self.transparent)
                if self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage7':
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
            elif self.c4['image'] == 'pyimage5':
                self.c4.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.c4['image'] == 'pyimage6':
                self.c4.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablec4 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.d3['image'] != 'pyimage3':
                    self.abled3 = False
                else:
                    self.abled3 = True
                if self.d3['image'] == 'pyimage2' or self.e2['image'] == 'pyimage3':
                    self.ablee2 = True
                else:
                    self.ablee2 = False
                if self.d5['image'] != 'pyimage3':
                    self.abled5 = False
                else:
                    self.abled5 = True
                if self.d5['image'] == 'pyimage2' or self.e6['image'] == 'pyimage3':
                    self.ablee6 = True
                else:
                    self.ablee6 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.b3['image'] != 'pyimage3':
                    self.ableb3 = False
                else:
                    self.ableb3 = True
                if self.b3['image'] == 'pyimage1' or self.a2['image'] == 'pyimage3':
                    self.ablea2 = True
                else:
                    self.ablea2 = False
                if self.b5['image'] != 'pyimage3':
                    self.ableb5 = False
                else:
                    self.ableb5 = True
                if self.b5['image'] == 'pyimage1' or self.a6['image'] == 'pyimage3':
                    self.ablea6 = True
                else:
                    self.ablea6 = False
        elif self.check and self.ablec4:
            if self.piece == 'red':
                self.c4.configure(image=self.redpiece)
                if self.b3['image'] == 'pyimage4':
                    self.b3.configure(image=self.transparent)
                elif self.b5['image'] == 'pyimage4':
                    self.b5.configure(image=self.transparent)
                elif self.b3['image'] == 'pyimage2' and self.a2['image'] == 'pyimage4':
                    self.b3.configure(image=self.transparent)
                    self.a2.configure(image=self.transparent)
                elif self.b5['image'] == 'pyimage2' and self.a6['image'] == 'pyimage4':
                    self.b5.configure(image=self.transparent)
                    self.a6.configure(image=self.transparent)
            elif self.piece == 'black':
                self.c4.configure(image=self.blackpiece)
                if self.d3['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
                elif self.d5['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage1' and self.e2['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
                    self.e2.configure(image=self.transparent)
                elif self.d5['image'] == 'pyimage1' and self.e6['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                    self.e6.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.c4.configure(image=self.redking)
                if self.b5['image'] == 'pyimage7':
                    self.b5.configure(image=self.transparent)
                elif self.d5['image'] == 'pyimage7':
                    self.d5.configure(image=self.transparent)
                if self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage7':
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.c4.configure(image=self.blackking)
                if self.b5['image'] == 'pyimage7':
                    self.b5.configure(image=self.transparent)
                elif self.d5['image'] == 'pyimage7':
                    self.d5.configure(image=self.transparent)
                if self.b3['image'] == 'pyimage7':
                    self.b3.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage7':
                    self.d3.configure(image=self.transparent)
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
            elif self.c6['image'] == 'pyimage5':
                self.c6.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.c6['image'] == 'pyimage6':
                self.c6.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablec6 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.d7['image'] != 'pyimage3':
                    self.abled7 = False
                else:
                    self.abled7 = True
                if self.d7['image'] == 'pyimage2' or self.e8['image'] == 'pyimage3':
                    self.ablee8 = True
                else:
                    self.ablee8 = False
                if self.d5['image'] != 'pyimage3':
                    self.abled5 = False
                else:
                    self.abled5 = True
                if self.d5['image'] == 'pyimage2' or self.e4['image'] == 'pyimage3':
                    self.ablee4 = True
                else:
                    self.ablee4 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.b7['image'] != 'pyimage3':
                    self.ableb7 = False
                else:
                    self.ableb7 = True
                if self.b7['image'] == 'pyimage1' or self.a8['image'] == 'pyimage3':
                    self.ablea8 = True
                else:
                    self.ablea8 = False
                if self.b5['image'] != 'pyimage3':
                    self.ableb5 = False
                else:
                    self.ableb5 = True
                if self.b5['image'] == 'pyimage1' and self.a4['image'] == 'pyimage3':
                    self.ablea4 = True
                else:
                    self.ablea4 = False
        elif self.check and self.ablec6:
            if self.piece == 'red':
                self.c6.configure(image=self.redpiece)
                if self.b5['image'] == 'pyimage4':
                    self.b5.configure(image=self.transparent)
                elif self.b7['image'] == 'pyimage4':
                    self.b7.configure(image=self.transparent)
                elif self.b7['image'] == 'pyimage2' and self.a8['image'] == 'pyimage4':
                    self.b7.configure(image=self.transparent)
                    self.a8.configure(image=self.transparent)
                elif self.b5['image'] == 'pyimage2' and self.a4['image'] == 'pyimage4':
                    self.b5.configure(image=self.transparent)
                    self.a4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.c6.configure(image=self.blackpiece)
                if self.d5['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage1' and self.e8['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
                    self.e8.configure(image=self.transparent)
                elif self.d5['image'] == 'pyimage1' and self.e4['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                    self.e4.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.c6.configure(image=self.redking)
                if self.b5['image'] == 'pyimage7':
                    self.b5.configure(image=self.transparent)
                elif self.d5['image'] == 'pyimage7':
                    self.d5.configure(image=self.transparent)
                if self.b7['image'] == 'pyimage7':
                    self.b7.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage7':
                    self.d7.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.c6.configure(image=self.blackking)
                if self.b5['image'] == 'pyimage7':
                    self.b5.configure(image=self.transparent)
                elif self.d5['image'] == 'pyimage7':
                    self.d5.configure(image=self.transparent)
                if self.b7['image'] == 'pyimage7':
                    self.b7.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage7':
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
            elif self.c8['image'] == 'pyimage5':
                self.c8.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.c8['image'] == 'pyimage6':
                self.c8.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablec8 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.d7['image'] != 'pyimage3':
                    self.abled7 = False
                else:
                    self.abled7 = True
                if self.d7['image'] == 'pyimage2' or self.e6['image'] == 'pyimage3':
                    self.ablee6 = True
                else:
                    self.ablee6 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.b7['image'] != 'pyimage3':
                    self.ableb7 = False
                else:
                    self.ableb7 = True
                if self.b7['image'] == 'pyimage1' or self.a6['image'] == 'pyimage3':
                    self.ablea6 = True
                else:
                    self.ablea6 = False
        elif self.check and self.ablec8:
            if self.piece == 'red':
                self.c8.configure(image=self.redpiece)
                if self.b7['image'] == 'pyimage4':
                    self.b7.configure(image=self.transparent)
                elif self.b7['image'] == 'pyimage2' and self.a6['image'] == 'pyimage4':
                    self.b7.configure(image=self.transparent)
                    self.a6.configure(image=self.transparent)
            elif self.piece == 'black':
                self.c8.configure(image=self.blackpiece)
                if self.d7['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage1' and self.e6['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
                    self.e6.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.c8.configure(image=self.redking)
                if self.b7['image'] == 'pyimage7':
                    self.b7.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage7':
                    self.d7.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.c8.configure(image=self.blackking)
                if self.b7['image'] == 'pyimage7':
                    self.b7.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage7':
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
            elif self.d1['image'] == 'pyimage5':
                self.d1.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.d1['image'] == 'pyimage6':
                self.d1.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.abled1 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.e2['image'] != 'pyimage3':
                    self.ablee2 = False
                else:
                    self.ablee2 = True
                if self.e2['image'] == 'pyimage2' or self.f3['image'] == 'pyimage3':
                    self.ablef3 = True
                else:
                    self.ablef3 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.c2['image'] != 'pyimage3':
                    self.ablec2 = False
                else:
                    self.ablec2 = True
                if self.c2['image'] == 'pyimage1' or self.b5['image'] == 'pyimage3':
                    self.ableb3 = True
                else:
                    self.ableb3 = False
        elif self.check and self.abled1:
            if self.piece == 'red':
                self.d1.configure(image=self.redpiece)
                if self.c2['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
                elif self.c2['image'] == 'pyimage2' and self.b3['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
                    self.b3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.d1.configure(image=self.blackpiece)
                if self.e2['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                elif self.e2['image'] == 'pyimage1' and self.f3['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                    self.f3.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.d1.configure(image=self.redking)
                if self.c2['image'] == 'pyimage7':
                    self.c2.configure(image=self.transparent)
                elif self.e2['image'] == 'pyimage7':
                    self.e2.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.d1.configure(image=self.blackking)
                if self.c2['image'] == 'pyimage7':
                    self.c2.configure(image=self.transparent)
                elif self.e2['image'] == 'pyimage7':
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
            elif self.d3['image'] == 'pyimage5':
                self.d3.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.d3['image'] == 'pyimage6':
                self.d3.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.abled3 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.e4['image'] != 'pyimage3':
                    self.ablee4 = False
                else:
                    self.ablee4 = True
                if self.e2['image'] != 'pyimage3':
                    self.ablee2 = False
                else:
                    self.ablee2 = True
                if self.e4['image'] == 'pyimage2' or self.f5['image'] == 'pyimage3':
                    self.ablef5 = True
                else:
                    self.ablef5 = False
                if self.e2['image'] == 'pyimage2' or self.f1['image'] == 'pyimage3':
                    self.ablef1 = True
                else:
                    self.ablef1 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.c4['image'] != 'pyimage3':
                    self.ablec4 = False
                else:
                    self.ablec4 = True
                if self.c2['image'] != 'pyimage3':
                    self.ablec2 = False
                else:
                    self.ablec2 = True
                if self.c4['image'] == 'pyimage1' or self.b5['image'] == 'pyimage3':
                    self.ableb5 = True
                else:
                    self.ableb5 = False
                if self.c2['image'] == 'pyimage1' or self.b1['image'] == 'pyimage3':
                    self.ableb1 = True
                else:
                    self.ableb1 = False
        elif self.check and self.abled3:
            if self.piece == 'red':
                self.d3.configure(image=self.redpiece)
                if self.c2['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
                elif self.c2['image'] == 'pyimage2' and self.b1['image'] == 'pyimage4':
                    self.c2.configure(image=self.transparent)
                    self.b1.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage2' and self.b5['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
                    self.b5.configure(image=self.transparent)
            elif self.piece == 'black':
                self.d3.configure(image=self.blackpiece)
                if self.e2['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                elif self.e2['image'] == 'pyimage1' and self.f1['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                    self.f1.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage1' and self.f5['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                    self.f5.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.d3.configure(image=self.redking)
                if self.c2['image'] == 'pyimage7':
                    self.c2.configure(image=self.transparent)
                elif self.e2['image'] == 'pyimage7':
                    self.e2.configure(image=self.transparent)
                if self.c4['image'] == 'pyimage7':
                    self.c4.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage7':
                    self.e4.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.d3.configure(image=self.blackking)
                if self.c2['image'] == 'pyimage7':
                    self.c2.configure(image=self.transparent)
                elif self.e2['image'] == 'pyimage7':
                    self.e2.configure(image=self.transparent)
                if self.c4['image'] == 'pyimage7':
                    self.c4.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage7':
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
            elif self.d5['image'] == 'pyimage5':
                self.d5.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.d5['image'] == 'pyimage6':
                self.d5.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.abled5 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.e4['image'] != 'pyimage3':
                    self.ablee4 = False
                else:
                    self.ablee4 = True
                if self.e6['image'] != 'pyimage3':
                    self.ablee6 = False
                else:
                    self.ablee6 = True
                if self.e4['image'] == 'pyimage2' or self.f3['image'] == 'pyimage3':
                    self.ablef3 = True
                else:
                    self.ablef7 = False
                if self.e6['image'] == 'pyimage2' or self.f7['image'] == 'pyimage3':
                    self.ablef7 = True
                else:
                    self.ablef7 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.c4['image'] != 'pyimage3':
                    self.ablec4 = False
                else:
                    self.ablec4 = True
                if self.c6['image'] != 'pyimage3':
                    self.ablec6 = False
                else:
                    self.ablec6 = True
                if self.c4['image'] == 'pyimage1' or self.b3['image'] == 'pyimage3':
                    self.ableb3 = True
                else:
                    self.ableb3 = False
                if self.c6['image'] == 'pyimage1' or self.b7['image'] == 'pyimage3':
                    self.ableb7 = True
                else:
                    self.ableb7 = False
        elif self.check and self.abled5:
            if self.piece == 'red':
                self.d5.configure(image=self.redpiece)
                if self.c4['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage2' and self.b7['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
                    self.b7.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage2' and self.b3['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
                    self.b3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.d5.configure(image=self.blackpiece)
                if self.e4['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage1' and self.f7['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                    self.f7.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage1' and self.f3['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                    self.f3.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.d5.configure(image=self.redking)
                if self.c6['image'] == 'pyimage7':
                    self.c6.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage7':
                    self.e6.configure(image=self.transparent)
                if self.c4['image'] == 'pyimage7':
                    self.c4.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage7':
                    self.e4.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.d5.configure(image=self.blackking)
                if self.c6['image'] == 'pyimage7':
                    self.c6.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage7':
                    self.e6.configure(image=self.transparent)
                if self.c4['image'] == 'pyimage7':
                    self.c4.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage7':
                    self.e4.configure(image=self.transparent)
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
            elif self.d7['image'] == 'pyimage5':
                self.d7.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.d7['image'] == 'pyimage6':
                self.d7.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.abled7 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.e8['image'] != 'pyimage3':
                    self.ablee8 = False
                else:
                    self.ablee8 = True
                    self.ablee6 = True
                if self.e6['image'] != 'pyimage3':
                    self.ablee6 = False
                else:
                    self.ablee8 = True
                    self.ablee6 = True
                if self.e6['image'] == 'pyimage2' or self.f5['image'] == 'pyimage3':
                    self.ablef5 = True
                else:
                    self.ablef5 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.c8['image'] != 'pyimage3':
                    self.ablec8 = False
                else:
                    self.ablec8 = True
                if self.c6['image'] != 'pyimage3':
                    self.ablec6 = False
                else:
                    self.ablec6 = True
                if self.c6['image'] == 'pyimage1' or self.b5['image'] == 'pyimage3':
                    self.ableb5 = True
                else:
                    self.ableb5 = False
        elif self.check and self.abled7:
            if self.piece == 'red':
                self.d7.configure(image=self.redpiece)
                if self.c8['image'] == 'pyimage4':
                    self.c8.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage2' and self.b5['image'] == 'pyimage4':
                    self.c6.configure(image=self.transparent)
                    self.b5.configure(image=self.transparent)
            elif self.piece == 'black':
                self.d7.configure(image=self.blackpiece)
                if self.e8['image'] == 'pyimage4':
                    self.e8.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage1' and self.f5['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                    self.f5.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.d7.configure(image=self.redking)
                if self.c6['image'] == 'pyimage7':
                    self.c6.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage7':
                    self.e6.configure(image=self.transparent)
                if self.c8['image'] == 'pyimage7':
                    self.c8.configure(image=self.transparent)
                elif self.e8['image'] == 'pyimage7':
                    self.e8.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.d7.configure(image=self.blackking)
                if self.c6['image'] == 'pyimage7':
                    self.c6.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage7':
                    self.e6.configure(image=self.transparent)
                if self.c8['image'] == 'pyimage7':
                    self.c8.configure(image=self.transparent)
                elif self.e8['image'] == 'pyimage7':
                    self.e8.configure(image=self.transparent)
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
            elif self.e2['image'] == 'pyimage5':
                self.e2.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.e2['image'] == 'pyimage6':
                self.e2.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablee2 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.f3['image'] != 'pyimage3':
                    self.ablef3 = False
                else:
                    self.ablef3 = True
                if self.f1['image'] != 'pyimage3':
                    self.ablef1 = False
                else:
                    self.ablef1 = True
                if self.f3['image'] == 'pyimage2' or self.g4['image'] == 'pyimage3':
                    self.ableg4 = True
                else:
                    self.ableg4 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.d3['image'] != 'pyimage3':
                    self.abled3 = False
                else:
                    self.abled3 = True
                if self.d3['image'] == 'pyimage1' or self.c4['image'] == 'pyimage3':
                    self.ablec4 = True
                else:
                    self.ablec4 = False
                if self.d1['image'] != 'pyimage3':
                    self.abled1 = False
                else:
                    self.abled1 = True
        elif self.check and self.ablee2:
            if self.piece == 'red':
                self.e2.configure(image=self.redpiece)
                if self.d1['image'] == 'pyimage4':
                    self.d1.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage2' and self.c4['image'] == 'pyimage4':
                    self.c4.configure(image=self.transparent)
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.e2.configure(image=self.blackpiece)
                if self.f1['image'] == 'pyimage4':
                    self.f1.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage1' and self.g4['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
                    self.g4.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.e2.configure(image=self.redking)
                if self.d1['image'] == 'pyimage7':
                    self.d1.configure(image=self.transparent)
                elif self.f1['image'] == 'pyimage7':
                    self.f1.configure(image=self.transparent)
                if self.d3['image'] == 'pyimage7':
                    self.d3.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage7':
                    self.f3.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.e2.configure(image=self.blackking)
                if self.d1['image'] == 'pyimage7':
                    self.d1.configure(image=self.transparent)
                elif self.f1['image'] == 'pyimage7':
                    self.f1.configure(image=self.transparent)
                if self.d3['image'] == 'pyimage7':
                    self.d3.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage7':
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
            elif self.e4['image'] == 'pyimage5':
                self.e4.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.e4['image'] == 'pyimage6':
                self.e4.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablee4 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.f3['image'] != 'pyimage3':
                    self.ablef3 = False
                else:
                    self.ablef3 = True
                if self.f5['image'] != 'pyimage3':
                    self.ablef5 = False
                else:
                    self.ablef5 = True
                if self.f3['image'] == 'pyimage2' or self.g2['image'] == 'pyimage3':
                    self.ableg2 = True
                else:
                    self.ableg2 = False
                if self.f5['image'] == 'pyimage2' or self.g6['image'] == 'pyimage3':
                    self.ableg6 = True
                else:
                    self.ableg6 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.d3['image'] != 'pyimage3':
                    self.abled3 = False
                else:
                    self.abled3 = True
                if self.d3['image'] == 'pyimage1' or self.c2['image'] == 'pyimage3':
                    self.ablec2 = True
                else:
                    self.ablec2 = False
                if self.d5['image'] != 'pyimage3':
                    self.abled5 = False
                else:
                    self.abled5 = True
                if self.d5['image'] == 'pyimage1' or self.c6['image'] == 'pyimage3':
                    self.ablec6 = True
                else:
                    self.ablec6 = False
        elif self.check and self.ablee4:
            if self.piece == 'red':
                self.e4.configure(image=self.redpiece)
                if self.d5['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                elif self.d3['image'] == 'pyimage4':
                    self.d3.configure(image=self.transparent)
                elif self.c2['image'] == 'pyimage4' and self.d3['image'] == 'pyimage2':
                    self.c2.configure(image=self.transparent)
                    self.d3.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage4' and self.d5['image'] == 'pyimage2':
                    self.c6.configure(image=self.transparent)
                    self.d5.configure(image=self.transparent)
            elif self.piece == 'black':
                self.e4.configure(image=self.blackpiece)
                if self.f5['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage1' and self.g2['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
                    self.g2.configure(image=self.transparent)
                elif self.f5['image'] == 'pyimage1' and self.g6['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                    self.g6.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.e4.configure(image=self.redking)
                if self.d5['image'] == 'pyimage7':
                    self.d5.configure(image=self.transparent)
                elif self.f5['image'] == 'pyimage7':
                    self.f5.configure(image=self.transparent)
                if self.d3['image'] == 'pyimage7':
                    self.d3.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage7':
                    self.f3.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.e4.configure(image=self.blackking)
                if self.d5['image'] == 'pyimage7':
                    self.d5.configure(image=self.transparent)
                elif self.f5['image'] == 'pyimage7':
                    self.f5.configure(image=self.transparent)
                if self.d3['image'] == 'pyimage7':
                    self.d3.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage7':
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
            elif self.e6['image'] == 'pyimage5':
                self.e6.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.e6['image'] == 'pyimage6':
                self.e6.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablee6 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.f7['image'] != 'pyimage3':
                    self.ablef7 = False
                else:
                    self.ablef7 = True
                if self.f5['image'] != 'pyimage3':
                    self.ablef5 = False
                else:
                    self.ablef5 = True
                if self.f7['image'] == 'pyimage2' or self.g8['image'] == 'pyimage3':
                    self.ableg8 = True
                else:
                    self.ableg8 = False
                if self.f5['image'] == 'pyimage2' or self.g4['image'] == 'pyimage3':
                    self.ableg4 = True
                else:
                    self.ableg4 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.d7['image'] != 'pyimage3':
                    self.abled7 = False
                else:
                    self.abled7 = True
                if self.d7['image'] == 'pyimage1' or self.c8['image'] == 'pyimage3':
                    self.ablec8 = True
                else:
                    self.ablec8 = False
                if self.d5['image'] != 'pyimage3':
                    self.abled5 = False
                else:
                    self.abled5 = True
                if self.d5['image'] == 'pyimage1' or self.c4['image'] == 'pyimage3':
                    self.ablec4 = True
                else:
                    self.ablec4 = False
        elif self.check and self.ablee6:
            if self.piece == 'red':
                self.e6.configure(image=self.redpiece)
                if self.d5['image'] == 'pyimage4':
                    self.d5.configure(image=self.transparent)
                elif self.d7['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
                elif self.c4['image'] == 'pyimage4' and self.d5['image'] == 'pyimage2':
                    self.c4.configure(image=self.transparent)
                    self.d5.configure(image=self.transparent)
                elif self.c8['image'] == 'pyimage4' and self.d7['image'] == 'pyimage2':
                    self.c8.configure(image=self.transparent)
                    self.d7.configure(image=self.transparent)
            elif self.piece == 'black':
                self.e6.configure(image=self.blackpiece)
                if self.f5['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage1' and self.g8['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
                    self.g8.configure(image=self.transparent)
                elif self.f5['image'] == 'pyimage1' and self.g4['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                    self.g4.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.e6.configure(image=self.redking)
                if self.d5['image'] == 'pyimage7':
                    self.d5.configure(image=self.transparent)
                elif self.f5['image'] == 'pyimage7':
                    self.f5.configure(image=self.transparent)
                if self.d7['image'] == 'pyimage7':
                    self.d7.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage7':
                    self.f7.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.e6.configure(image=self.blackking)
                if self.d5['image'] == 'pyimage7':
                    self.d5.configure(image=self.transparent)
                elif self.f5['image'] == 'pyimage7':
                    self.f5.configure(image=self.transparent)
                if self.d7['image'] == 'pyimage7':
                    self.d7.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage7':
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
            elif self.e8['image'] == 'pyimage5':
                self.e8.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.e8['image'] == 'pyimage6':
                self.e8.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablee8 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.f7['image'] != 'pyimage3':
                    self.ablef7 = False
                else:
                    self.ablef7 = True
                if self.f7['image'] == 'pyimage2' or self.g6['image'] == 'pyimage3':
                    self.ableg6 = True
                else:
                    self.ableg6 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.d7['image'] != 'pyimage3':
                    self.abled7 = False
                else:
                    self.abled7 = True
                if self.d7['image'] == 'pyimage1' or self.c6['image'] == 'pyimage3':
                    self.ablec6 = True
                else:
                    self.ablec6 = False
        elif self.check and self.ablee8:
            if self.piece == 'red':
                self.e8.configure(image=self.redpiece)
                if self.d7['image'] == 'pyimage4':
                    self.d7.configure(image=self.transparent)
                elif self.c6['image'] == 'pyimage4' and self.d7['image'] == 'pyimage2':
                    self.c6.configure(image=self.transparent)
                    self.d7.configure(image=self.transparent)
            elif self.piece == 'black':
                self.e8.configure(image=self.blackpiece)
                if self.f7['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage1' and self.g6['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
                    self.g6.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.e8.configure(image=self.redking)
                if self.d7['image'] == 'pyimage7':
                    self.d7.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage7':
                    self.f7.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.e8.configure(image=self.blackking)
                if self.d7['image'] == 'pyimage7':
                    self.d7.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage7':
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
            elif self.f1['image'] == 'pyimage5':
                self.f1.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.f1['image'] == 'pyimage6':
                self.f1.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablef1 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.g3['image'] != 'pyimage3':
                    self.ableg3 = False
                else:
                    self.ableg3 = True
                if self.g3['image'] == 'pyimage2' or self.h4['image'] == 'pyimage3':
                    self.ableh4 = True
                else:
                    self.ableh4 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.e2['image'] != 'pyimage3':
                    self.ablee2 = False
                else:
                    self.ablee2 = True
                if self.e2['image'] == 'pyimage1' or self.d3['image'] == 'pyimage3':
                    self.abled3 = True
                else:
                    self.abled3 = False
        elif self.check and self.ablef1:
            if self.piece == 'red':
                self.f1.configure(image=self.redpiece)
                if self.e2['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                elif self.e2['image'] == 'pyimage2' and self.d3['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.f1.configure(image=self.blackpiece)
                if self.g2['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                elif self.g2['image'] == 'pyimage1' and self.h3['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                    self.h3.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.f1.configure(image=self.redking)
                if self.e2['image'] == 'pyimage7':
                    self.e2.configure(image=self.transparent)
                elif self.g2['image'] == 'pyimage7':
                    self.g2.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.f1.configure(image=self.blackking)
                if self.e2['image'] == 'pyimage7':
                    self.e2.configure(image=self.transparent)
                elif self.g2['image'] == 'pyimage7':
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
            elif self.f3['image'] == 'pyimage5':
                self.f3.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.f3['image'] == 'pyimage6':
                self.f3.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablef3 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.g2['image'] != 'pyimage3':
                    self.ableg2 = False
                else:
                    self.ableg2 = True
                if self.g2['image'] == 'pyimage2' or self.h1['image'] == 'pyimage3':
                    self.ableh1 = True
                else:
                    self.ableh1 = False
                if self.g4['image'] != 'pyimage3':
                    self.ableg4 = False
                else:
                    self.ableg4 = True
                if self.g4['image'] == 'pyimage2' or self.h5['image'] == 'pyimage3':
                    self.ableh5 = True
                else:
                    self.ableh5 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.e4['image'] != 'pyimage3':
                    self.ablee4 = False
                else:
                    self.ablee4 = True
                if self.e4['image'] == 'pyimage1' or self.d3['image'] == 'pyimage3':
                    self.abled3 = True
                else:
                    self.abled3 = False
                if self.e2['image'] != 'pyimage3':
                    self.ablee2 = False
                else:
                    self.ablee2 = True
                if self.e2['image'] == 'pyimage1' or self.d1['image'] == 'pyimage3':
                    self.abled1 = True
                else:
                    self.abled1 = False
        elif self.check and self.ablef3:
            if self.piece == 'red':
                self.f3.configure(image=self.redpiece)
                if self.e2['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                elif self.e2['image'] == 'pyimage2' and self.d1['image'] == 'pyimage4':
                    self.e2.configure(image=self.transparent)
                    self.d1.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage2' and self.d5['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                    self.d5.configure(image=self.transparent)
            elif self.piece == 'black':
                self.f3.configure(image=self.blackpiece)
                if self.g2['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
                elif self.g2['image'] == 'pyimage1' and self.h1['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                    self.h1.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage1' and self.h5['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
                    self.h5.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.f3.configure(image=self.redking)
                if self.e2['image'] == 'pyimage7':
                    self.e2.configure(image=self.transparent)
                elif self.g2['image'] == 'pyimage7':
                    self.g2.configure(image=self.transparent)
                if self.e4['image'] == 'pyimage7':
                    self.e4.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage7':
                    self.g4.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.f3.configure(image=self.blackking)
                if self.e2['image'] == 'pyimage7':
                    self.e2.configure(image=self.transparent)
                elif self.g2['image'] == 'pyimage7':
                    self.g2.configure(image=self.transparent)
                if self.e4['image'] == 'pyimage7':
                    self.e4.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage7':
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
            elif self.f5['image'] == 'pyimage5':
                self.f5.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.f5['image'] == 'pyimage6':
                self.f5.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablef5 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.g6['image'] != 'pyimage3':
                    self.ableg6 = False
                else:
                    self.ableg6 = True
                if self.g6['image'] == 'pyimage2' or self.h7['image'] == 'pyimage3':
                    self.ableh7 = True
                else:
                    self.ableh7 = False
                if self.g4['image'] != 'pyimage3':
                    self.ableg4 = False
                else:
                    self.ableg4 = True
                if self.g4['image'] == 'pyimage2' or self.h3['image'] == 'pyimage3':
                    self.ableh3 = True
                else:
                    self.ableh3 = False
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.e6['image'] != 'pyimage3':
                    self.ablee6 = False
                else:
                    self.ablee6 = True
                if self.e6['image'] == 'pyimage1' or self.d7['image'] == 'pyimage3':
                    self.abled7 = True
                else:
                    self.abled7 = False
                if self.e4['image'] != 'pyimage3':
                    self.ablee4 = False
                else:
                    self.ablee4 = True
                if self.e4['image'] == 'pyimage1' and self.d3['image'] == 'pyimage3':
                    self.abled3 = True
                else:
                    self.abled3 = False
        elif self.check and self.ablef5:
            if self.piece == 'red':
                self.f5.configure(image=self.redpiece)
                if self.e6['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage2' and self.d7['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                    self.d7.configure(image=self.transparent)
                elif self.e4['image'] == 'pyimage2' and self.d3['image'] == 'pyimage4':
                    self.e4.configure(image=self.transparent)
                    self.d3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.f5.configure(image=self.blackpiece)
                if self.g6['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
                elif self.g6['image'] == 'pyimage1' and self.h7['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                    self.h7.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage1' and self.h3['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
                    self.h3.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.f5.configure(image=self.redking)
                if self.e6['image'] == 'pyimage7':
                    self.e6.configure(image=self.transparent)
                elif self.g6['image'] == 'pyimage7':
                    self.g6.configure(image=self.transparent)
                if self.e4['image'] == 'pyimage7':
                    self.e4.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage7':
                    self.g4.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.f5.configure(image=self.blackking)
                if self.e6['image'] == 'pyimage7':
                    self.e6.configure(image=self.transparent)
                elif self.g6['image'] == 'pyimage7':
                    self.g6.configure(image=self.transparent)
                if self.e4['image'] == 'pyimage7':
                    self.e4.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage7':
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
            elif self.f7['image'] == 'pyimage5':
                self.f7.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.f7['image'] == 'pyimage6':
                self.f7.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ablef7 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.g6['image'] != 'pyimage3':
                    self.ableg6 = False
                else:
                    self.ableg6 = True
                if self.g6['image'] == 'pyimage2' or self.h5['image'] == 'pyimage3':
                    self.ableh5 = True
                else:
                    self.ableh5 = False
                if self.g8['image'] != 'pyimage3':
                    self.ableg8 = False
                else:
                    self.ableg8 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.e8['image'] != 'pyimage3':
                    self.ablee8 = False
                else:
                    self.ablee8 = True
                if self.e6['image'] != 'pyimage3':
                    self.ablee6 = False
                else:
                    self.ablee6 = True
                if self.e6['image'] == 'pyimage1' or self.d5['image'] == 'pyimage3':
                    self.abled5 = True
                else:
                    self.abled5 = False
        elif self.check and self.ablef7:
            if self.piece == 'red':
                self.f7.configure(image=self.redpiece)
                if self.e6['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                elif self.e8['image'] == 'pyimage4':
                    self.e8.configure(image=self.transparent)
                elif self.e6['image'] == 'pyimage2' and self.d5['image'] == 'pyimage4':
                    self.e6.configure(image=self.transparent)
                    self.d5.configure(image=self.transparent)
            elif self.piece == 'black':
                self.f7.configure(image=self.blackpiece)
                if self.g6['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                elif self.g8['image'] == 'pyimage4':
                    self.g8.configure(image=self.transparent)
                elif self.g6['image'] == 'pyimage1' and self.h5['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                    self.h5.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.f7.configure(image=self.redking)
                if self.e6['image'] == 'pyimage7':
                    self.e6.configure(image=self.transparent)
                elif self.g6['image'] == 'pyimage7':
                    self.g6.configure(image=self.transparent)
                if self.e8['image'] == 'pyimage7':
                    self.e8.configure(image=self.transparent)
                elif self.g8['image'] == 'pyimage7':
                    self.g8.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.f7.configure(image=self.blackking)
                if self.e6['image'] == 'pyimage7':
                    self.e6.configure(image=self.transparent)
                elif self.g6['image'] == 'pyimage7':
                    self.g6.configure(image=self.transparent)
                if self.e8['image'] == 'pyimage7':
                    self.e8.configure(image=self.transparent)
                elif self.g8['image'] == 'pyimage7':
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
            elif self.g2['image'] == 'pyimage5':
                self.g2.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.g2['image'] == 'pyimage6':
                self.g2.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableg2 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.h1['image'] != 'pyimage3':
                    self.ableh1 = False
                else:
                    self.ableh1 = True
                if self.h3['image'] != 'pyimage3':
                    self.ableh3 = False
                else:
                    self.ableh3 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.f1['image'] != 'pyimage3':
                    self.ablef1 = False
                else:
                    self.ablef1 = True
                if self.f3['image'] != 'pyimage3':
                    self.ablef3 = False
                else:
                    self.ablef3 = True
                if self.f3['image'] == 'pyimage1' or self.e4['image'] == 'pyimage3':
                    self.ablee4 = True
                else:
                    self.ablee4 = False
        elif self.check and self.ableg2:
            if self.piece == 'red':
                self.g2.configure(image=self.redpiece)
                if self.f1['image'] == 'pyimage4':
                    self.f1.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage2' and self.e4['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
                    self.e4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.g2.configure(image=self.blackpiece)
                if self.h1['image'] == 'pyimage4':
                    self.h1.configure(image=self.transparent)
                elif self.h3['image'] == 'pyimage4':
                    self.h3.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.g2.configure(image=self.redking)
                if self.f1['image'] == 'pyimage7':
                    self.f1.configure(image=self.transparent)
                elif self.h1['image'] == 'pyimage7':
                    self.h1.configure(image=self.transparent)
                if self.f3['image'] == 'pyimage7':
                    self.f3.configure(image=self.transparent)
                elif self.h3['image'] == 'pyimage7':
                    self.h3.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.g2.configure(image=self.blackking)
                if self.f1['image'] == 'pyimage7':
                    self.f1.configure(image=self.transparent)
                elif self.h1['image'] == 'pyimage7':
                    self.h1.configure(image=self.transparent)
                if self.f3['image'] == 'pyimage7':
                    self.f3.configure(image=self.transparent)
                elif self.h3['image'] == 'pyimage7':
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
            elif self.g4['image'] == 'pyimage5':
                self.g4.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.g4['image'] == 'pyimage6':
                self.g4.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableg4 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.h5['image'] != 'pyimage3':
                    self.ableh5 = False
                else:
                    self.ableh5 = True
                if self.h3['image'] != 'pyimage3':
                    self.ableh3 = False
                else:
                    self.ableh3 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.f5['image'] != 'pyimage3':
                    self.ablef5 = False
                else:
                    self.ablef5 = True
                if self.f5['image'] == 'pyimage1' or self.e6['image'] == 'pyimage3':
                    self.ablee6 = True
                else:
                    self.ablee6 = False
                if self.f3['image'] != 'pyimage3':
                    self.ablef3 = False
                else:
                    self.ablef3 = True
                if self.f3['image'] == 'pyimage1' or self.e2['image'] == 'pyimage3':
                    self.ablee2 = True
                else:
                    self.ablee2 = False
        elif self.check and self.ableg4:
            if self.piece == 'red':
                self.g4.configure(image=self.redpiece)
                if self.f5['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
                elif self.f3['image'] == 'pyimage2' and self.e2['image'] == 'pyimage4':
                    self.f3.configure(image=self.transparent)
                    self.e2.configure(image=self.transparent)
                elif self.f5['image'] == 'pyimage2' and self.e6['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                    self.e6.configure(image=self.transparent)
            elif self.piece == 'black':
                self.g4.configure(image=self.blackpiece)
                if self.h5['image'] == 'pyimage4':
                    self.h5.configure(image=self.transparent)
                elif self.h3['image'] == 'pyimage4':
                    self.h3.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.g4.configure(image=self.redking)
                if self.f5['image'] == 'pyimage7':
                    self.f5.configure(image=self.transparent)
                elif self.h5['image'] == 'pyimage7':
                    self.h5.configure(image=self.transparent)
                if self.f3['image'] == 'pyimage7':
                    self.f3.configure(image=self.transparent)
                elif self.h3['image'] == 'pyimage7':
                    self.h3.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.g4.configure(image=self.blackking)
                if self.f5['image'] == 'pyimage7':
                    self.f5.configure(image=self.transparent)
                elif self.h5['image'] == 'pyimage7':
                    self.h5.configure(image=self.transparent)
                if self.f3['image'] == 'pyimage7':
                    self.f3.configure(image=self.transparent)
                elif self.h3['image'] == 'pyimage7':
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
            elif self.g6['image'] == 'pyimage5':
                self.g6.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.g6['image'] == 'pyimage6':
                self.g6.configure(image=self.purpleking)
                self.piece = 'blackking'
            self.check = True
            self.ableg6 = True
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.h5['image'] != 'pyimage3':
                    self.ableh5 = False
                else:
                    self.ableh5 = True
                if self.h7['image'] != 'pyimage3':
                    self.ableh7 = False
                else:
                    self.ableh7 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.f5['image'] != 'pyimage3':
                    self.ablef5 = False
                else:
                    self.ablef5 = True
                if self.f5['image'] == 'pyimage1' or self.e4['image'] == 'pyimage3':
                    self.ablee4 = True
                else:
                    self.ablee4 = False
                if self.f7['image'] != 'pyimage3':
                    self.ablef7 = False
                else:
                    self.ablef7 = True
                if self.f7['image'] == 'pyimage1' or self.e8['image'] == 'pyimage3':
                    self.ablee8 = True
                else:
                    self.ablee8 = False
        elif self.check and self.ableg6:
            if self.piece == 'red':
                self.g6.configure(image=self.redpiece)
                if self.f5['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage2' and self.e8['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
                    self.e8.configure(image=self.transparent)
                elif self.f5['image'] == 'pyimage2' and self.e4['image'] == 'pyimage4':
                    self.f5.configure(image=self.transparent)
                    self.e4.configure(image=self.transparent)
            elif self.piece == 'black':
                self.g6.configure(image=self.blackpiece)
                if self.h5['image'] == 'pyimage4':
                    self.h5.configure(image=self.transparent)
                elif self.h7['image'] == 'pyimage4':
                    self.h7.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.g6.configure(image=self.redking)
                if self.f5['image'] == 'pyimage7':
                    self.f5.configure(image=self.transparent)
                elif self.h5['image'] == 'pyimage7':
                    self.h5.configure(image=self.transparent)
                if self.f7['image'] == 'pyimage7':
                    self.f7.configure(image=self.transparent)
                elif self.h7['image'] == 'pyimage7':
                    self.h7.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.g6.configure(image=self.blackking)
                if self.f5['image'] == 'pyimage7':
                    self.f5.configure(image=self.transparent)
                elif self.h5['image'] == 'pyimage7':
                    self.h5.configure(image=self.transparent)
                if self.f7['image'] == 'pyimage7':
                    self.f7.configure(image=self.transparent)
                elif self.h7['image'] == 'pyimage7':
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
            if self.piece == 'red' or self.piece == 'redking' or self.piece == 'blackking':
                if self.h7['image'] != 'pyimage3':
                    self.ableh7 = False
                else:
                    self.ableh7 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.f7['image'] != 'pyimage3':
                    self.ablef7 = False
                else:
                    self.ablef7 = True
                if self.f7['image'] == 'pyimage1' or self.e6['image'] == 'pyimage3':
                    self.ablee6 = True
                else:
                    self.ablee6 = False
        elif self.check and self.ableg8:
            if self.piece == 'red':
                self.g8.configure(image=self.redpiece)
                if self.f7['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
                elif self.f7['image'] == 'pyimage2' and self.e6['image'] == 'pyimage4':
                    self.f7.configure(image=self.transparent)
                    self.e6.configure(image=self.transparent)
            elif self.piece == 'black':
                self.g8.configure(image=self.blackpiece)
                if self.h7['image'] == 'pyimage4':
                    self.h7.configure(image=self.transparent)
            elif self.piece == 'redking':
                self.g8.configure(image=self.redking)
                if self.f7['image'] == 'pyimage7':
                    self.f7.configure(image=self.transparent)
                elif self.h7['image'] == 'pyimage7':
                    self.h7.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.g8.configure(image=self.blackking)
                if self.f7['image'] == 'pyimage7':
                    self.f7.configure(image=self.transparent)
                elif self.h7['image'] == 'pyimage7':
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
            elif self.h1['image'] == 'pyimage5':
                self.h1.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.h1['image'] == 'pyimage6':
                self.h1.configure(image=self.purpleking)
            self.check = True
            self.ableh1 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.g2['image'] != 'pyimage3':
                    self.ableg2 = False
                else:
                    self.ableg2 = True
                if self.g2['image'] == 'pyimage1' and self.f3['image'] == 'pyimage3':
                    self.ablef3 = True
                else:
                    self.ablef3 = False
        elif self.check and self.ableh1:
            if self.piece == 'red':
                self.h1.configure(image=self.redking)
                if self.g2['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                elif self.g2['image'] == 'pyimage2' and self.f3['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                    self.f3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.h1.configure(image=self.blackpiece)
            elif self.piece == 'redking':
                self.h1.configure(image=self.redking)
                if self.g2['image'] == 'pyimage7':
                    self.g2.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.h1.configure(image=self.blackking)
                if self.g2['image'] == 'pyimage7':
                    self.g2.configure(image=self.transparent)
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
            elif self.h3['image'] == 'pyimage5':
                self.h3.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.h3['image'] == 'pyimage6':
                self.h3.configure(image=self.purpleking)
            self.check = True
            self.ableh3 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.g2['image'] != 'pyimage3':
                    self.ableg2 = False
                else:
                    self.ableg2 = True
                if self.g2['image'] == 'pyimage1' or self.f1['image'] == 'pyimage3':
                    self.ablef1 = True
                else:
                    self.ablef1 = False
                if self.g4['image'] != 'pyimage3':
                    self.ableg4 = False
                else:
                    self.ableg4 = True
                if self.g4['image'] == 'pyimage1' or self.f5['image'] == 'pyimage3':
                    self.ablef5 = True
                else:
                    self.ablef5 = False
        elif self.check and self.ableh3:
            if self.piece == 'red':
                self.h3.configure(image=self.redking)
                if self.g2['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
                elif self.g2['image'] == 'pyimage2' and self.f1['image'] == 'pyimage4':
                    self.g2.configure(image=self.transparent)
                    self.f1.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage2' and self.f5['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
                    self.f5.configure(image=self.transparent)
            elif self.piece == 'black':
                self.h3.configure(image=self.blackpiece)
            elif self.piece == 'redking':
                self.h3.configure(image=self.redking)
                if self.g2['image'] == 'pyimage7':
                    self.g2.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage7':
                    self.g4.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.h3.configure(image=self.blackking)
                if self.g2['image'] == 'pyimage7':
                    self.g2.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage7':
                    self.g4.configure(image=self.transparent)
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
            elif self.h5['image'] == 'pyimage5':
                self.h5.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.h5['image'] == 'pyimage6':
                self.h5.configure(image=self.purpleking)
            self.check = True
            self.ableh5 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.g6['image'] != 'pyimage3':
                    self.ableg6 = False
                else:
                    self.ableg6 = True
                if self.g6['image'] == 'pyimage1' or self.f7['image'] == 'pyimage3':
                    self.ablef7 = True
                else:
                    self.ablef7 = False
                if self.g4['image'] != 'pyimage3':
                    self.ableg4 = False
                else:
                    self.ableg4 = True
                if self.g4['image'] == 'pyimage1' or self.f3['image'] == 'pyimage3':
                    self.ablef3 = True
                else:
                    self.ablef3 = False
        elif self.check and self.ableh5:
            if self.piece == 'red':
                self.h5.configure(image=self.redking)
                if self.g6['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
                elif self.g6['image'] == 'pyimage2' and self.f7['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                    self.f7.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage2' and self.f3['image'] == 'pyimage4':
                    self.g4.configure(image=self.transparent)
                    self.f3.configure(image=self.transparent)
            elif self.piece == 'black':
                self.h5.configure(image=self.blackpiece)
            elif self.piece == 'redking':
                self.h5.configure(image=self.redking)
                if self.g6['image'] == 'pyimage7':
                    self.g6.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage7':
                    self.g4.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.h5.configure(image=self.blackking)
                if self.g6['image'] == 'pyimage7':
                    self.g6.configure(image=self.transparent)
                elif self.g4['image'] == 'pyimage7':
                    self.g4.configure(image=self.transparent)
            self.piece = ''
            self.check = False
            self.clear()

    def moveh7(self):
        if not self.check:
            if self.h7['image'] == 'pyimage1':
                self.h7.configure(image=self.purplepiece)
                self.piece = 'red'
            elif self.h7['image'] == 'pyimage2':
                self.h7.configure(image=self.purplepiece)
                self.piece = 'black'
            elif self.h7['image'] == 'pyimage5':
                self.h7.configure(image=self.purpleking)
                self.piece = 'redking'
            elif self.h7['image'] == 'pyimage6':
                self.h7.configure(image=self.purpleking)
            self.check = True
            self.ableh7 = True
            if self.piece == 'black' or self.piece == 'redking' or self.piece == 'blackking':
                if self.g6['image'] != 'pyimage3':
                    self.ableg6 = False
                else:
                    self.ableg6 = True
                if self.g6['image'] == 'pyimage1' or self.f5['image'] == 'pyimage3':
                    self.ablef5 = True
                else:
                    self.ablef5 = False
                if self.g8['image'] != 'pyimage3':
                    self.ableg8 = False
                else:
                    self.ableg8 = True
        elif self.check and self.ableh7:
            if self.piece == 'red':
                self.h7.configure(image=self.redking)
                if self.g6['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                elif self.g8['image'] == 'pyimage4':
                    self.g8.configure(image=self.transparent)
                elif self.g6['image'] == 'pyimage2' and self.f5['image'] == 'pyimage4':
                    self.g6.configure(image=self.transparent)
                    self.f5.configure(image=self.transparent)
            elif self.piece == 'black':
                self.h7.configure(image=self.blackpiece)
            elif self.piece == 'redking':
                self.h5.configure(image=self.redking)
                if self.g6['image'] == 'pyimage7':
                    self.g6.configure(image=self.transparent)
                elif self.g8['image'] == 'pyimage7':
                    self.g8.configure(image=self.transparent)
            elif self.piece == 'blackking':
                self.h5.configure(image=self.blackking)
                if self.g6['image'] == 'pyimage7':
                    self.g6.configure(image=self.transparent)
                elif self.g8['image'] == 'pyimage7':
                    self.g8.configure(image=self.transparent)
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


root = tk.Tk()
root.title("Checkers")
root.geometry("304x328")
app = Checkers(root)
root.mainloop()
