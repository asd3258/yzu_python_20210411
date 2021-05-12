# 非對稱結構資料
e1 = {'name': 'John', 'salary': 50000, 'progran':['HTML', 'JS']}
e2 = {'name': 'Mary', 'salary': 60000, 'progran':['HTML', 'Python']}
e3 = {'name': 'Bob', 'salary': 70000, 'progran':['Java', 'Python', 'C#']}
# 計算會Python的員工人名, 並將放入到names = [] 中
emps = [e1, e2, e3]
# print(emps['progran'])
target = 'Python'
names = []
for emp in emps:
    # print(emp['name'], emp['progran'])
    for p in emp['progran']:
        if p == target:
            print(emp['name'], p)
            names.append(emp['name'])
print(names)

