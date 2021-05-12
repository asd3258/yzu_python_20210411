# 數組:list(元素可重複) set(元素不可重複) dict(key/value)
import random as r
scores = [100, -10, 90, -80, 999]  # list
# error_scores = scores.pop(1)
# print(error_scores, scores)
# error_scores = scores.pop(3)
# print(error_scores, scores)

# 練習 取出不要的數值
# 利用pop 挑出不合法
error_scores = []
for i in scores:
    if i < 0 or i > 100:
        error_scores.append(i)
print(scores)
print(error_scores)

for e in error_scores:
    scores.pop(scores.index(e))
print(scores)

scores = [1, 3, 5, 7]
# 反轉
scores.reverse()
print(scores)

# 排序
scores.sort()
print(scores)

# 洗牌 需要先import random
r.shuffle(scores)
print(scores)

