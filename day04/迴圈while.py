import random as r
while True:
    n = r.randint(1, 100)
    if n % 3 == 0:
        print(n)
        continue  # 當成立則繼續執行迴圈, 不執行剩下程式碼
    if n == 50:
        print('移開迴圈, n=', n)
        break  # 跳離迴圈

