import tkinter as tk
import class0219

class win():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("BMI WORK")
        self.window.geometry('600x480')
        self.BMI=class0219.ww()
        self.label1=tk.Label(self.window,text='您的身高')
        self.label1.grid(column=0,row=0)
        self.box1=tk.Entry(self.window)
        self.box1.grid(column=1,row=0)
        self.label2=tk.Label(self.window,text='您的體重')
        self.label2.grid(column=2,row=0)
        self.box2=tk.Entry(self.window)
        self.box2.grid(column=3,row=0)
        self.btn=tk.Button(self.window,text='確定',command=self.aaa).grid(column=2,row=1)
        self.label3=tk.Label(self.window,text='BMI=')
        self.label3.grid(column=4 ,row=10)
        self.window.mainloop()

    def aaa(self):
        self.label3.config(text=self.BMI.printInfo(self.box1.get(),self.box2.get()))

main = win()