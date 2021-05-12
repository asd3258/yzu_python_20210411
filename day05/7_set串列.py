import random as r

# lotto = set()  # 不重複元素的串列
# lotto.add(10)
# lotto.add(10)
# lotto.add(20)
# print(len(lotto), lotto)

# 取出不重複5個號碼
lotto = set()
while len(lotto) < 5:
    n = r.randint(1, 39)
    lotto.add(n)

print(len(lotto), lotto)
