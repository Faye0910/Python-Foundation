#import 檔案名稱    等同include
''' t1=檔案名稱   d=t1.abc(c)就是取檔案名稱內的abc function'''

a=5
b="str"
c="str"
print(a)
print(type(a))  #ptint(type(a))會出現型態像是int...
print(type(b))
                          # &&變成 and    、 ||變成or
if(a==5 and b=="str"):    #if else的{}都改成:   排版要排好不然會掛掉.. '''(多行註解)或者#(單行註解)
    print("bbb")
    print("a not 9")
else:
    print(a)


a=['123','abc','asdf','qwer']
len(a[0])           #取長度
a[0]
a[-1]               #取最後一個
print(c)
print("----------------------")
a_dict = {'name': 'Ben', 'height': 178}
print(a_dict['height'])

no = [1,2,3,4,5,6,7,8,9]

for a in no:     #看in什麼 假如改成range(5) 就只會顯示0~4   如果要用if比較常用while  no就是在上面陣列的範圍
    print(a)
print("----------------------")

def test(c):             # def就是自訂函式 c是接收的值
    abc="abc"+c
    return abc

s=test(c)
print(s)
