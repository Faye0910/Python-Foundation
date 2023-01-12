import tkinter as tk
import classhomework

fileName="test.txt"
class abc:
    def __init__(self):
        self.AAA = classhomework.file()
        self.window = tk.Tk()
        self.window.title("WORK")
        self.window.geometry('600x480')
        self.label1 = tk.Label(self.window, text='輸入')
        self.label1.grid(column=0, row=0)
        self.box1 = tk.Entry(self.window)
        self.box1.grid(column=1, row=0)
        self.label2 = tk.Label(self.window, text='')
        self.label2.grid(column=2, row=2)
        self.btn = tk.Button(self.window, text='確定', command=self.rr).grid(column=2, row=1)
        self.window.mainloop()
    def rr(self):
        c = self.box1.get()
        print(self.AAA.read(fileName))
        self.label2.config(text=self.AAA.open(c))

main=abc()