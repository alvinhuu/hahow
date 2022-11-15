# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:17:20 2019

@author: Ivan
"""

import pandas as pd


'''
製作 Dataframe  資料集 member
'''
# 作法一
data = {'uid':[1,2,3,4,5],
        'name':['Jack','Lily','Kevin',
                'Jojo','Harry'],
        'age':[25,21,35,18,15]}
       

member = pd.DataFrame(data)
member # 因為有這行才會在右邊Ipython 顯示


'''
查看前五筆資料
'''
member.head()

'''
查看欄位資訊
'''
# 欄位資訊
member.info()

# (列數,欄數)  (R,C)  直欄橫列 
member.shape

'''
修改欄位名稱
'''
# 怕同學後面會錯誤 複製一個df出來
test = member #.copy()

test.columns

test.columns =  ['num','word','fix']

# 前面的member也會受到影響哦
test 
member 


member = pd.DataFrame(data)


'''
取得一欄或多攔資料
'''

# df[‘columename’]
member['name']

# 多個欄位使用list包起來
member[ ['name','age']]

# 同上
colname = ['name','age']
member[colname]


#
### 問題：取出 uid 與age 欄位
colname = ['uid','age']
member[colname]

member[['uid','age']]

'''
常見計算
'''
member['age']

# 平均會員年紀
member['age'].mean()

# 最大會員年紀
member['age'].max()

# 最小會員年紀
member['age'].min()

# 其他常見統計
member['age'].describe()

# 排序(遞增)
member['age'].sort_values()

# 排序(遞減)
member['age'].sort_values(ascending = False)


'''
移除欄位 drop
'''
# drop
member.drop(columns=['uid'])


#
### 問題移除 uid 與 age
member.drop(columns=['uid','age'])

'''
把所有的值轉回陣列
'''
member.values.tolist()


'''
整欄資料型別轉換
'''
member['age'] = member['age'].astype('float64')
member['age'] 

member['age'] = member['age']
member['age'] .astype('int')

member.to_csv('member.csv',encoding='utf-8')
