# John = key 50000 = value   數組
salary = {'John': 50000, 'Mary': 60000}
print(salary)
print('John的薪資:', salary['John'])
for key in salary:
    print("%s 的薪資 %d" % (key, salary[key]))

salary.setdefault('Bob', 70000)  # 新增元素
print(salary)

# 求薪資總和

print(type(salary['John']))
print(salary['John'] + salary['Mary'] + salary['Bob'])

sum = 0
for key in salary:
    sum = sum + salary[key]
print(sum)
