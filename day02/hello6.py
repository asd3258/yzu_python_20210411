# -*- coding:UTF-8 -*-
import math
print(math.pow(2, 3))  #平方
print(math.sqrt(4))  #平方根

x1, y1 = 10, 20
x2, y2 = 15, 45
# 求兩點間距離d=?

a = math.pow(x1-x2, 2)
b = math.pow(y1-y2, 2)
c= math.sqrt(a+b)
print("%.1f" % c)

print((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5 )


