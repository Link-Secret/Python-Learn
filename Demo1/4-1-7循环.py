#@Time  :   2018/4/1 17:41
#@Author:   zjl
#@File  :   4-1-7循环.py

names = ['a','b','c']
for name in names:
    print(name)

for name in ['a','b','c']:
    print(name)

# Python提供一个range()函数，可以生成一个整数序列
print(list(range(10)))


# while
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']

for l in L:
    print(l)

i = 0
while i < 3:
    print(L[i])
    i += 1

i = 0
while i < 1:
    print(i)
    i -= 1