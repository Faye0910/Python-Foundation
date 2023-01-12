class ww():
    def printInfo(self,a,b):
            a=float(a)
            b=float(b)
            BMI = 0
            BMI = float(b / ((a / 100) * (a / 100)))
            if (BMI >= 24):
                return ("過重")
            if (BMI < 24 and BMI > 17):
                return ("正常")
            if (BMI <= 17):
                return ("過輕")