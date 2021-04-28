def getChickenAndRabbit(sum, feet):
    '''
    :param sum:
    :param feet:
    :return:
    '''
    if feet/4 <= sum <= feet/2:
        rabbbit = (feet - sum *2)/2
        chicken = sum - rabbbit
        return chicken, rabbbit
    else:
        print('無法計算')
        return 0, 0

print(getChickenAndRabbit(83, 240))
c, r = getChickenAndRabbit(100, 240)
print(c, r)
