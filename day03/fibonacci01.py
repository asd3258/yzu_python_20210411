#費式數列遞迴求解

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = 3
value = fib(n)
print(n, value)


a = 6/2*(1 + 2)
print(a)

x = True
y = False
z = False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)


x =1
y =1
g = 240
while x < 60:
    while y <60:
        z = 2 * x + 4 * y
        if z == g:
            print(x, y)
    y = y + 1
x = x + 1

