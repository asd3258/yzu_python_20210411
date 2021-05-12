# 數組:list(元素可重複) set(元素不可重複) dict(key/value)

scores = [20, 30, 10]  # list
scores.append(50)
print(scores)
scores.insert(0, 10)
print(scores)
scores.append([70, 75])  # 加入不捨去自己的維度 [10, 20, 30, 10, 50, [70, 75]]
print(scores)
print(scores[5][0])  # 取2維元素
scores.extend([80, 82])  # 加入捨去自己的維度 [10, 20, 30, 10, 50, [70, 75], 80, 82]
print(scores)
