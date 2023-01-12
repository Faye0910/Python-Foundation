import numpy as np
import time
import cv2
import tkinter as tk
from PIL import ImageTk,Image



class aaa():
    def __init__(self):
        self.np1 = np.array([1, 3, 2, 5, 3, 1, 2])
        self.aaaa = [1, 3, 2, 5, 3, 1, 2]

        self.img = cv2.imread("1mgPic.jpg")
        self.eimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.im = Image.fromarray(self.eimg)


        self.w=len(self.eimg)
        self.h=len(self.eimg[0])
        self.np2 = np.array(self.img)


        self.window = tk.Tk()
        self.window.title("WORK")
        self.window.geometry('600x480')

        self.btn = tk.Button(self.window, text='取代成0', command=self.num).pack()
        self.btn1 = tk.Button(self.window, text='等於3個數', command=self.nnnn).pack()
        self.btn4 = tk.Button(self.window, text='>=3', command=self.big).pack()
        self.button = tk.Button(self.window, text='確定', command=self.qqq)
        self.button.pack()
        self.label1 = tk.Label(self.window, text='')
        self.label1.pack()
        self.label2 = tk.Label(self.window, text='')
        self.label2.pack()
        self.window.mainloop()
    def num(self):
        stat=time.time()
        time.sleep(1)
        self.np2[self.np2 >= 130] = 255
        end = time.time()

        #==================================================================================
        stat1 = time.time()
        time.sleep(1)
        for x in range(self.w):
            for y in range(self.h):
                if (self.img[x][y][0] >= 130):
                    self.img[x][y][0]=255
                if (self.img[x][y][1] >= 130):
                    self.img[x][y][1]=255
                if (self.img[x][y][2] >= 130):
                    self.img[x][y][2]=255
        end1 = time.time()

        print("時間:"+str(end-stat))        #取代成零
        print("\r\n時間:" + str(end1 - stat1))


    def nnnn(self):
        a=0
        stat = time.time()
        time.sleep(1)
        a=np.sum(self.np2 == 0)
        end=time.time()

        # ================================================================================
        c = 0
        stat1 = time.time()
        time.sleep(1)
        for x in range(self.w):
            for y in range(self.h):
                if (self.img[x][y][0] == 0):
                    c=c+1
                if (self.img[x][y][1] == 0):
                    c=c+1
                if (self.img[x][y][2] ==0):
                    c=c+1
        end1 = time.time()

        print("數量:"+str(a)+"     時間:"+str(end-stat))
        print("數量:"+str(c)+"     時間:"+str(end1-stat1))    #等於0
    def big(self):
        a=0
        stat = time.time()
        time.sleep(1)
        a =np.sum(self.np2 >= 130)
        end = time.time()
        #==================================================================================
        xx = 0
        stat1 = time.time()
        time.sleep(1)
        for x in range(self.w):
            for y in range(self.h):
                if(self.img[x][y][0]>=130):
                    xx=xx+1
                if (self.img[x][y][1]>=130):
                    xx=xx+1
                if (self.img[x][y][2]>=130):
                    xx=xx+1
        end1 = time.time()

        print("數量:" + str(a) + "     時間:" + str(end - stat))
        print("數量:" + str(xx) + "     時間:" + str(end1 - stat1))        #大於等於3
    def qqq(self):
            self.oimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            print(self.oimg)
            im = Image.fromarray(self.oimg)  # 放在圖片陣列
            img2 = ImageTk.PhotoImage(image=im)
            self.label1 = tk.Label(image=img2)
            self.label1.image = img2
            self.label1.pack()
main=aaa()