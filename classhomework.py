import os.path

class file():
    def read(self,fileName):
        if (os.path.isfile(fileName)):  # 假如有找到fileName的東西就執行
            self.fileObject = open(fileName, 'r')  # 打開檔案讀
            self.aa="已開啟檔案"
            self.data={}
            return self.aa
    def open(self,abc):
        if(self.aa=="已開啟檔案"):

            ROW = self.fileObject.readline()
            c = ROW.find(":")
            d = ROW.find("\n")
            a = ROW[0:c]
            b = ROW[(c + 1):d]
            self.data.setdefault(a, b)

            while(ROW!=""):
                    ROW = self.fileObject.readline()
                    c=ROW.find(":")
                    d = ROW.find("\n")
                    a=ROW[0:c]
                    b=ROW[(c+1):d]
                    if (a != "" and b != ""):
                        self.data.setdefault(a,b)
            try:
                return(self.data[abc])
            except:
                return("error")
            #self.data={}
            #return (self.data) # 顯示
            #print(self.data['x'])
            #print  ( "dict['x']: ", dict['x'])
        self.fileObject.close()