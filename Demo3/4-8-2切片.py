#@Time  :   2018/4/8 19:44
#@Author:   zjl
#@File  :   4-8-2切片.py

L = list(range(100))

# 取前十个数字
L[:10]

# 取后十个数字
L[-10:]

# 10 - 20数字
L[10:20]

# 前十个，且相隔2
L[:10:2]

# 所有数，相隔5个取
L[::5]

# 复制一份
L[:]

# ----------------------------------------------------------------
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：


# *********************************************************************
# 练习题       利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    return s[1:-1]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')