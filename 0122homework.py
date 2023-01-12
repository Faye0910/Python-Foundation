import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk
import cv2
img=cv2.imread("123.png") #先讀取檔案
def printInfo4():
    a = str(box6.get())
    img=cv2.imread(a)
    cv2.imshow('my image',img)
def printInfo2():
    a = str(box6.get())
    img = cv2.imread(a)
    cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
    cv2.imshow('my image2', img)
    cv2.imwrite('abc.jpg', img)



def printInfo():
    try:
        BMI=0
        a=float(box1.get())
        b=float(box2.get())
        BMI=float(b/((a/100)*(a/100)))
        if(BMI>=24):
            label3.config(text="過重")
        if (BMI < 24 and BMI>17):
            label3.config(text="正常")
        if (BMI<=17):
            label3.config(text="過輕")
    except ValueError:
        tk.messagebox.showinfo(message="輸入錯誤")


def printInfo3():
    try:
        a=float(box3.get())
        b=float(box4.get())
        c = float(box5.get())

        if(a>=b and a>=c):
            if(a*a==b*b+c*c):
                label8.config(text="是直角三角形")
            else:
                label8.config(text="NO")
        if (b >= a and b >= c):
            if (b * b == a * a + c * c):
                label8.config(text="是直角三角形")
            else:
                label8.config(text="NO")
        if (c >= b and c >= a):
            if (c * c == b * b + a * a):
                label8.config(text="是直角三角形")
            else:
                label8.config(text="NO")
    except ValueError:
        tk.messagebox.showinfo(message="輸入錯誤")
#========視窗設定=============
window=tk.Tk()
window.title("BMI WORK")
window.geometry('600x480')

tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='BMI')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='三角形')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='畫圖存檔')

#====================================================================================================
label1=ttk.Label(tab1,text='您的身高')
label1.grid(column=0,row=0)

box1=ttk.Entry(tab1)
box1.grid(column=1,row=0)

label2=ttk.Label(tab1,text='您的體重')
label2.grid(column=2,row=0)

box2=ttk.Entry(tab1)
box2.grid(column=3,row=0)

btn=ttk.Button(tab1,text='確定',command=printInfo).grid(column=2,row=1)

label3=ttk.Label(tab1,text='BMI=')
label3.grid(column=4 ,row=10)

tabControl.pack(expand=1, fill="both")
#==================================================================================

label4=tk.Label(tab2,text='請輸入三個數')
label4.grid(column=0,row=0)

label5=tk.Label(tab2,text='A')
label5.grid(column=0,row=1)

box3=tk.Entry(tab2)
box3.grid(column=1,row=1)

label6=tk.Label(tab2,text='B')
label6.grid(column=0,row=2)

box4=tk.Entry(tab2)
box4.grid(column=1,row=2)

label7=tk.Label(tab2,text='C')
label7.grid(column=0,row=3)

box5=tk.Entry(tab2)
box5.grid(column=1,row=3)


label8=tk.Label(tab2,text='ans')
label8.grid(column=0,row=4)

btn=tk.Button(tab2,text='確定',command=printInfo3).grid(column=2,row=4)
tabControl.pack(expand=1, fill="both")
#=============================================
label9=tk.Label(tab3,text='輸入檔案路徑')
label9.pack()

box6=tk.Entry(tab3)
box6.pack()

btnnn=tk.Button(tab3,text='顯示圖檔',command=printInfo4).pack()
btn2=tk.Button(tab3,text='畫斜線',command=printInfo2).pack()
tabControl.pack(expand=1, fill="both")

window.mainloop()