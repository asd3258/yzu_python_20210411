# 數組:list(元素可重複) set(元素不可重複) dict(key/value)
scores = [100, 90, 80]  # list
scores.append(70)
print(scores)
print(scores[1])  # 取得維度1
print(len(scores))  # 取得元素個數
print(scores.index(80))  # 取得某個元素的維度值
print(max(scores))  # 取得元素最大值
print(min(scores))  # 取得元素最小值
print(max(scores), min(scores))
# 走訪每一個元素I
for x in scores:
    print(x)
# 走訪每一個元素II
for (idx, value) in enumerate(scores):
    print(idx, value)



