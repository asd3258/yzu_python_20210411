import math

def getBMI(h, w):
    bmi = w / math.pow(h/100, 2)
    return bmi

def getResult(bmi):
    result = "過輕"
    if 18 <= bmi <= 23:
        result = "正常"
    elif bmi >23:
        result = "過重"
    return result

def getBMIAndResult(h, w):
    bmi = getBMI(h, w)
    result = getResult(bmi)
    return bmi, result

bmi1 = getBMI(170, 60)  #呼叫getBMI→計算bmi後回傳給bmi1
bmi2 = getBMI(180, 90)
print(bmi1, bmi2)

bmi3, result3 = getBMIAndResult(170, 60)
bmi4, result4 = getBMIAndResult(180, 90)
print(bmi3, result3)
print(bmi4, result4)
print("bmi3=%.2f result3=%s" % (bmi3, result3))
print("bmi4=%.2f result4=%s" % (bmi4, result4))
