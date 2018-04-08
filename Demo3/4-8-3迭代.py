#@Time  :   2018/4/8 19:54
#@Author:   zjl
#@File  :   4-8-3迭代.py

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
# 而我们不太关心该对象究竟是list还是其他数据类型。

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

# 练习

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

# -*- coding: utf-8 -*-
def findMinAndMax(L):
        if L == []:
            return (None,None)
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            elif i > max:
                max = i
        return (min,max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')