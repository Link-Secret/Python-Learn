#@Time  :   2018/4/1 16:01
#@Author:   zjl
#@File  :   05.列表.py

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
# classmates = ['no1','no2','no3']
# print(classmates[-1])
# print(len(classmates))

# tuple 元组 初始化就不可更改 不可插入 不能赋值 代码更安全

print("-----元组")

# Python在显示只有1个元素的tuple时，也会加一个逗号,
# t=(1,)
# st = (1)
#
# # t[0] = 3
# st = (3)
#
# print(t)
# print(st)

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！


# 练习
#
# 请用索引取出下面list的指定元素：
#
# # -*- coding: utf-8 -*-
#
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#
# # 打印Apple:
# print(?)
# # 打印Python:
# print(?)
# # 打印Lisa:
# print(?)

print(L[0][0])
print(L[1][1])
print(L[2][2])


print(L + ['test1','test2']);
print(L + [['test1','test2']]);


# 总结：
#   有序集合list classmates['a','b','c']        取出来 classmates[1]
#   元组tuple    l('a','b','c')                       l[1]
# set   {'1','2'}                                   无序
# dict 字典  {key:value,key2:value2}                 无序，通过key访问，key必须为不可变的，和元组一样

