# -*- coding:UTF-8 -*-
h = 170
w = 60
bmi = w / (h/100)**2
print(bmi)
print("%.2f" % bmi)

# // = 取整數
print(5/2)  #=2.5
print(5//2)  #=2
# % = 餘數
print(5%2)  #=1

num = 123456789
if num % 2 == 0:
    print("偶數")
else:
    print("奇數")


