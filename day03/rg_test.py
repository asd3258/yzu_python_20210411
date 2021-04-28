# -*- coding:UTF-8 -*-
a = True or False
print(a)

c = False and False
print(c)

b = True or False and False
print(b)

import random as r
n = r.randint(1, 99)
result = "偶數" if n % 2 == 0 else "奇數"
print(n, result)
print(n, "是", result)
print(str(n) + "是" + result)

