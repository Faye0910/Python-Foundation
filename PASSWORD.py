import tkinter as tk
from random import randint
import PASSWORD2
class abc:
    def __init__(self):
        self.lowest = 1
        self.highest = 99
        if(self.highest==100):
            self.highest=99
        self.AAA=PASSWORD2.password()
        self.answer = randint(self.lowest, self.highest)
        print(self.answer)
        self.window = tk.Tk()
        self.window.title("PASSWORD")
        self.window.geometry('600x480')
        self.label1=tk.Label(self.window,text='猜數字',font=("Helvetica",20))
        self.label1.pack()
        self.label2 = tk.Label(self.window, text='1-99', font=("Helvetica",20))
        self.label2.pack()
        self.box1 = tk.Entry(self.window)
        self.box1.pack()
        self.btn = tk.Button(self.window, text='確定',command=self.gu).pack()
        self.btn2 = tk.Button(self.window, text='重新', command=self.aa).pack()
        self.window.mainloop()
    def gu(self):
        guess=self.box1.get()
        try:
            guess=int(guess)
        except:
            self.label1.config(text='請輸入數字')
            return

        textt=self.AAA.abc(guess,self.lowest,self.highest,self.answer)

        if(textt.find('-')<0):
            self.label2.config(text=str(textt))
        else:
            le = (textt.index('-'))
            self.lowest = (textt[0:le] + "\n")
            self.highest = (textt[(le + 1):])
            self.label2.config(text=str(textt))

    def aa(self):
        self.lowest = 1
        self.highest = 100
        self.answer = randint(self.lowest, self.highest)
        print(self.answer)
        self.label2.config(text='1-99', font=("Helvetica", 20))

main=abc()