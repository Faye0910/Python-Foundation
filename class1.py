import tkinter as tk
import class2
class abc:
    def __init__(self):
        self.AAA = class2.subb()
        self.window = tk.Tk()
        self.window.title("WORK")
        self.window.geometry('600x480')
        self.label1=tk.Label(self.window,text='輸入數字')
        self.label1.grid(column=0, row=0)
        self.box1 = tk.Entry(self.window)
        self.box1.grid(column=1, row=0)
        self.label2 = tk.Label(self.window, text='輸入數字').grid(column=0, row=1)
        self.box2 = tk.Entry(self.window)
        self.box2.grid(column=1, row=1)
        self.label3=tk.Label(self.window,text='答案').grid(column=2, row=2)
        self.label4=tk.Label(self.window,text='0')
        self.label4.grid(column=2, row=3)
        self.btn = tk.Button(self.window, text='+', command=self.aaa).grid(column=3, row=8)
        self.btn2 = tk.Button(self.window, text='-', command=self.bbb).grid(column=5, row=8)
        self.btn3 = tk.Button(self.window, text='*', command=self.ccc).grid(column=7, row=8)
        self.btn4 = tk.Button(self.window, text='/', command=self.ddd).grid(column=9, row=8)
        self.window.mainloop()
    def aaa(self):
        a=self.box1.get()
        b=self.box2.get()
        self.label4.config(text=(self.AAA.sub(a,b)))
    def bbb(self):
        a = self.box1.get()
        b = self.box2.get()
        self.label4.config(text=self.AAA.D(a,b))
    def ccc(self):
        a = self.box1.get()
        b = self.box2.get()
        self.label4.config(text=self.AAA.X(text=self.AAA.D(a,b)))
    def ddd(self):
        a = self.box1.get()
        b = self.box2.get()
        self.label4.config(text=self.AAA.Z(text=self.AAA.D(a,b)))

main=abc()