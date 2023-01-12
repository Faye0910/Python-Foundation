import tkinter as tk
from tkinter import messagebox

class addbutton():
    def __init__(self):
        self.btnlist=[]
        self.btnnum=0
#==============tk介面===================
        self.window=tk.Tk()
        self.window.title("新增按鈕")
        self.window.geometry('480x600')

        self.frameone=tk.Frame(self.window)
        self.frameone.pack()
        self.button1=tk.Button(self.window,text='新增按鈕',command=self.newbtn)
        self.button1.pack()
        self.box1 = tk.Entry(self.window)
        self.box1.pack()
        self.button2 = tk.Button(self.window, text='刪除按鈕', command=self.btndele)
        self.button2.pack()

        self.window.mainloop()

    def newbtn(self):
        self.btnlist.append(tk.Button(self.window))
        self.btnlist[self.btnnum].pack()
        self.btnlist[self.btnnum].config(text='btn'+str(self.btnnum),command=lambda a=self.btnnum:self.btnprint(a))
        self.btnnum=self.btnnum+1

    def btnprint(self,num):
        self.num=num
        print(num)
    def btndele(self):
         try: 
            self.a=int(self.box1.get())
         except:
            tk.messagebox.showinfo(message="輸入錯誤")

         self.btnlist[self.a].destroy()
         del self.btnlist[self.a]


main=addbutton()