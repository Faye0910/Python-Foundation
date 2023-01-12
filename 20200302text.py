import threading
import time
#===============================   thread   =======================================
class thread:
    def __init__(self):
        self.lock=threading.Lock()
    def aaa(self):
        a=1
        for i in range(10):
            a=a+1
            print("thread1:"+str(a))
            time.sleep(1)
    def bbb(self):
        b=0
        for i in range(10):
            b=b+1
            print("thread2:"+str(b))
            time.sleep(2)

    def test(self):

        t1=threading.Thread(target=self.aaa)
        t1.start()                              #如果加入join()就會執行完前面的執行續在執行之後的

        t2 = threading.Thread(target=self.bbb)  #,args=(b,)裡面有一個參數要加,不然會掛
        t2.start()
t=thread()
main=t.test()
#=====================================================================================