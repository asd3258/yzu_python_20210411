# -*- coding:UTF-8 -*-

str = 'she sell sea shell on the sea shore'

str = str.strip()  # 除去左右空白
str = str.lstrip()  # 除去左空白
str = str.rstrip()  # 除去右空白

print('字串長度:', len(str))
print('有幾個S:', str.count('s'))
print('on這個字的位置:', str.find('on'))
print('off這個字的位置:', str.find('off'))
print('有沒有sea這個字:', '有' if str.find('sea') >= 0 else '沒有')
print('有沒有land這個字:', '有' if str.find('land') >= 0 else '沒有')
print('有幾個單字:', str.count(' ') + 1)
#  是否都是英文字(a-z A-Z)
print('是否都是英文字', str.isalpha())
print('是否都是英文字', str.replace(' ', '').isalpha())

print(str[2])  # 取出第3個字
print(str[:3])  # 取出0~3個字(不含3)
print(str[0:3])  # 取出0~3個字(不含3)
print(str[1:3])  # 取出1~3個字(不含3)

path = 'c:\temp\nba\score.py'
print('路徑位置:', path)
path = r'c:\temp\nba\score.py'  # 原始字串r
print('路徑位置:', path)

