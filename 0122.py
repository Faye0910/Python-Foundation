import tkinter as tk
import tkinter.ttk as ttk

def btnClick():
    label1.config(text='紅包滿滿')
def printInfo():
    selection=''
    for i in checkbox:
        if checkbox[i].get()==True:
            selection=selection+season[i]+"\t"
    print(selection)

#========視窗設定=============
window=tk.Tk()
window.title("test")
window.geometry('600x480')

label1=tk.Label(window,text='20200122')
label1.pack()

btn1=tk.Button(window,text='CLICK',command=btnClick)
btn1.pack()

label2=tk.Label(window,text='////////')
label2.pack()

season={0:'春季',1:'夏季',2:'秋季',3:'冬季'}
checkbox={}
for  i in range(len(season)):
    checkbox[i]=tk.BooleanVar()
    tk.Checkbutton(window,text=season[i],variable=checkbox[i]).pack()
ckBtn=tk.Button(window,text='確定',width=12,command=printInfo).pack()

window.mainloop()
