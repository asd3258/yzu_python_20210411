# -*- coding:UTF-8 -*-
# 隨機亂數
import random
n = random.randrange(0, 5)  # 0 <= 5 (0, 1, 2, 3, 4)
print(n)
n = random.randint(0, 5)   # 0 <= n <= 5 (0, 1, 2, 3, 4, 5)
print(n)

# 電腦選號
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
print(n1, n2, n3, n4)

# 跳脫字元
print("小明\n明天\t要\'結婚\'了")
# 想要印出 小明\n明天\t要\'結婚\'了
print("小明\\n明天\\t要\\'結婚\\'了")
print("""小明\n明天\t要\'結婚\'了""")

