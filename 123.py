#!/usr/bin/env python
# coding: utf-8

# ## <font color = green>FBA 02- 探索式資料分析</font>
# ### 首先讀入 東森新聞的粉絲專頁利用Python的Facebook API所抓取的9975篇文章 
# ### 觀測期間：2017/3~2017/6
# 

# In[1]:


import pandas as pd
df = pd.read_excel("birth.xlsx")


# ### 觀察一下前5筆資料  <font color=red>特別注意一下time欄位的格式</font>

# In[2]:


df.head(5)


# ### 觀察一下DataFrame的info(), 同時檢查是否有null存在, 可以見到context欄位有7筆null資料

# In[3]:


df.info()
df.isnull().sum()


# ### 將context欄位為null的資料改成"無", 再檢查一次null
# ### DataFrame 常用數學函數如下
# 函數名稱 | 意義
# ---------|:-----
# count()  | 非NA的資料筆數 
# sum()    | 總和
# mean()   | 平均
# median() | 中位數
# min()    | 最小值
# idmin()  | 最小值的index值
# max()    | 最大值
# idmax()  | 最大值的index值
# abs()    | 絕對值
# std()    | 標準差
# var()    | 變異數
# 
# 
# 
# 

# In[4]:





# ### 計算按讚數量加總(一共有6種)

# In[5]:


df['likes_count'] = df['likes']+df['love']+df['wow']+df['haha']+df['angry']+df['sad']


# In[10]:


df.head(5)


# ### 準備處理time欄位格式, 先看原本的格式

# In[11]:


df['time'][0]


# ### 先將<font color=red>'T' 與 '-' 符號</font>從字串中移除

# In[12]:


df['time'] = df["time"].str.replace("T",'').str.replace("-",'')
df['time'][0]


# ### 接著將<font color=red> ':' </font>移除, 然後將+0000移除, 利用<font color=red>split()指定用'+'切開</font>, 應該得到兩項, 我們只要第1項

# In[13]:


df['time'] = df['time'].str.replace(':','').str.split('+').str[0]

df['time'][0]


# ### 將time欄位轉換為Pandas的datetime格式

# In[14]:


df['time'] = pd.to_datetime(df['time'],format='%Y%m%d%H%M%S')

df['time'][0]


# ### 將time欄位轉換為GMT+8(台灣的時區)的時間

# In[15]:


import datetime
df['time'] = df['time']+datetime.timedelta(hours = 8)
df['time'][0]


# ### 將time欄位的hour單獨建立成hour欄位, 方便依據發文時間做統計

# In[16]:


df['hour'] = df["time"].dt.hour
df['hour'] = df['hour'].astype('object')

df['hour'][0]


# ### 依據time欄位建立weekday欄位, 方便依據發文時間(周一至周日)做統計

# In[17]:


df['weekday'] = df["time"].dt.weekday
df['weekday'] = df['weekday'].replace([0, 1, 2, 3, 4, 5, 6], ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])

df['weekday'][0]


# ### 重新檢查一下DataFrame結構 

# In[18]:


df.info()


# In[19]:


df.head(3)


# ### 準備找出文章中的小編, 請先觀察文章中小編出現的特徵
# ### 可以發現是<font color=red>第1個#</font>, 後面接小編名字(一定是XX編), <font color=red>後面再接'：'</font>(注意是全形符號喔)

# In[20]:


curator = []
for i in df['context'].str.split('#').str[1].str.split('：').str[0]:
    try:
        if i[-1] == '編':
            curator.append(i)
        else:
            curator.append(None)
    except:
        curator.append(None)


# ### 建立curator欄位存放小編資訊

# In[21]:


df['curator'] = curator

df.head(3)


# ### 資料處理準備完成, 準備進行分析與繪圖 

# In[22]:


import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# In[23]:


from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:/windows/Fonts/msjh.ttc")


# In[24]:


df.describe()


# ### 依據curator欄位, 用value_counts()計算小編出現的次數, 就是發文篇數
# ### 可以用value_counts(ascending=True)將結果由小到大排列
# ### 可以用value_counts(normalize=True)將結果由次數改成百分比

# In[25]:


df['curator'].value_counts()


# In[26]:


df['curator'].value_counts(normalize=True)


# In[27]:


len(df['curator'].value_counts().index)


# ### Seaborn是一種基於matplotlib的圖形可視化python library, 以下使用seaborn的countplot圖
# ### 列出發文量前10名的小編

# In[28]:


sns.countplot(data=df, x='curator',   
              order=df['curator'].value_counts().iloc[:10].index)
plt.xticks(fontproperties=font, size=10)
plt.title("小編發文數量", fontproperties=font, size=12)
plt.show()


# 

# In[29]:


likes_avg = []
for i in df['curator'].value_counts().index:
    likes_avg.append([i,(df[df['curator']==i])["likes_count"].mean()])
print(likes_avg)
df2 = pd.DataFrame(likes_avg, columns=['curator','mean_likes'])
print(df2)
df3 = df2.sort_values('mean_likes',ascending=False).head(10)
sns.barplot(x='curator', y='mean_likes', data=df3)
plt.xticks(fontproperties=font, size=10)
plt.title("按讚數量前10名小編", fontproperties=font, size=12)
plt.show()


# ### 發文時間統計, <font color=red>半夜3-5點無發文</font>

# In[30]:


sns.countplot(data=df, x='hour')
plt.xticks(fontproperties=font, size=10)
plt.title("發文時間統計", fontproperties=font, size=12)
plt.show()


# ### 各時段按讚發文統計

# In[31]:


likes_avg_hour = []
for i in df['hour'].value_counts().index:
    likes_avg_hour.append([i,(df[df['hour']==i])["likes_count"].mean()])
df4 = pd.DataFrame(likes_avg_hour, columns=['hour','mean_likes'])
sns.barplot(x='hour', y='mean_likes', data=df4)
plt.xticks(fontproperties=font, size=10)
plt.title("各時段發文按讚成效", fontproperties=font, size=12)
plt.show()


# ### 以發文星期作為統計

# In[32]:


sns.countplot(data=df, x='weekday')
plt.xticks(fontproperties=font, size=10)
plt.title("發文星期統計", fontproperties=font, size=12)
plt.show()


# ### 查看各個星期發文按讚成效

# In[33]:


likes_avg_week = []
for i in df['weekday'].value_counts().index:
    likes_avg_week.append([i,(df[df['weekday']==i])["likes_count"].mean()])
df4 = pd.DataFrame(likes_avg_week, columns=['weekday','mean_likes'])
sns.barplot(x='weekday', y='mean_likes', data=df4)
plt.xticks(fontproperties=font,size=10)
plt.title("各星期發文按讚成效",fontproperties=font,size=12)
plt.show()


# ### 熱點圖 Heatmap   
# ### 各個星期 vs 各個時間點的發文數量

# In[34]:


df6 = pd.crosstab(df["hour"], df["weekday"])
sns.heatmap(df6, annot=True,cmap="Oranges")
plt.show()


# ### 各個星期 vs 各個時間點的按讚數量

# In[35]:


df7 = pd.pivot_table(df, index=['hour'], columns=['weekday'], 
                     values=['likes_count'])
sns.heatmap(df7, annot=True, cmap="Oranges")
plt.show()


# ### 最後將所有整理好的資料匯出

# In[36]:


df.to_excel("fanpage_clean.xlsx", index=False)

