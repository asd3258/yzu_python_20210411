# 轉換:list 與 Tuple
a = [1, 2, 3, 4, 5]  #可修改
b = (1, 2, 3, 4, 5)  #不可修改
a = tuple(a)
print(type(a), a)
b = list(b)
print(type(b), b)
