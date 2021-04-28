# -*- coding:UTF-8 -*-
# 千分位加小數點

n = 123 * 123 * 321
print(n)

print("{:,}".format(n))  #轉換後為字串
print("%.2f" % n )  #小數點後2位
print("{:,}".format(float("%.2f" % n )))  #第一種寫法
print(format(float("%.2f" % n), ","))  ##第二種寫法



