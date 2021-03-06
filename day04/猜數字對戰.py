import random as r
ans = 47
min = 0
max = 100

count = 50
while count > 0:
    # 使用者猜
    guess = int(input('(%d). 請輸入 %d ~ %d : ' % (count, min, max)))
    # 檢查 guess 的資料是否在min 與 max 之間?
    if guess >= max or guess <= min:
        print('數字範圍錯誤')
        continue

    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('使用者答對了')
        break

    # 電腦猜
    guess = r.randint(min+1, max-1)
    print('(%d). 電腦猜 %d ~ %d : %d ' % (count, min, max, guess))
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('電腦答對了')
        break

    count = count - 1

