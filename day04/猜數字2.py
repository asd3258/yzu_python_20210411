import random as r
ans = 47
min = 0
max = 100


count = 5
while count > 0:
    guess = int(input('(%d). 請輸入 %d ~ %d : ' % (count, min, max)))
    # 檢查 guess 的資料是否在min 與 max 之間?
    if guess >= max or guess <= min:
        print('數字範圍錯誤')
        continue
    count = count - 1

    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('答對了')
        break


