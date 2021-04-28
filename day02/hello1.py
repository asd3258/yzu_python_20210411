# -*- coding:UTF-8 -*- #中文
print ("我是中文")

# Python 保留字
import keyword
print(keyword.kwlist)



# = 單行註解, ctrl+/ = 註解
'''
    多行註解
    判斷成績是否及格
'''

score = 80
if score >= 60:
    print(score, "及格")
else:
    print(score, "不及格")

a12 = 12 # 10進位  不遵循P1P8標準
a13 = 12  # 10進位  有遵循P1P8標準

# 整數 8 10 16進位
a = 12  # 10進位
b = 0o12  # 8進位 零歐12
c = 0x12  # 16進位 零叉12
print(a, b, c)

# 浮點數
a = 3.14
b = 3.14e2  # 科學記號: 3.14e2 = 3.14 * 10**2 = 314.0
c = 1000e-2  # 科學記號: 1000e-2 = 1000 * 10*-2 = 10.0
print(a, b, c)

# 賦值(=)
name, h, w, age, isPass = 'John', 170.1, 60, 18, False
print(name, h, w, age, isPass)

# 資料型態 (type)
print(name, type(name))
print(h, type(h))
print(w, type(w))
print(age, type(age))
print(isPass, type(isPass))

# 刪除變數
money = 1234
print(money)
del money
print(money)








