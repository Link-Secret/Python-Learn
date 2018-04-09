#@Time  :   2018/4/9 16:35
#@Author:   zjl
#@File  :   4-9-4MapReduce.py

# map()函数   map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
#                   并把结果作为新的Iterator返回。
from functools import reduce


def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8])
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r))



# reduce()函数

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 示例1
def add(x,y):
    return x+y

m = reduce(add,[1,2,3,4,5,6,7])
print(m)

# 示例2  将str转换成int相当于int()函数的作用
def f2(x,y):
    return x*10+y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

# map函数调用char2num 将字符串转换成[1,2,3,6,7],通过reduce函数转换成12367
t = reduce(f2,map(char2num,'12367'))
print(t)
print(type(t))




# 练习

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    name = name.lower()
    name = name[0:1].upper()+name[1:]
    return name

print(normalize('XXXX'))

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 练习2：
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def X(x,y):
    return x*y

def prod(L):
    return reduce(X,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习3：利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def power2(x,n):
    for i in range(n):
        x = x * 10
    return x

def str2float(s):
    count = s.find('.')        #找到. 我将这个改进了，既可以判断浮点数，又可以判断整数
    if count != -1:
        s = s[:count]+s[count+1:]
    print(s)
    print(count)
    def fn(x, y):
            return x * 10 + y
    def char2num2(s):
        return DIGITS[s]
    if count != -1:
        return (reduce(fn, map(char2num2, s)))/(power2(1,count))
    else:
        return reduce(fn, map(char2num2, s))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


print("000000000000000000")
print(power2(10,0))



# 自我练习  实现int()函数

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2INT(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))  #map(char2num,s),将s对应的字符转换成[,,,,]然后使用reduce叠加使用

print(str2INT('1237890'))
