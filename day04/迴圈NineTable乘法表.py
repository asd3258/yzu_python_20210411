# x*y=z
# 1*1=1 1*2=2...1*9=9
# ...
# 9*1=9 9*2=18...9*9=81
for x in range(1, 10):
    for y in range(1, 10):
        z = x * y
        print("%02d * %02d = %02d" % (x, y, z), end=(" "))
    print()




