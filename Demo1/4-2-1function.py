#@Time  :   2018/4/2 15:41
#@Author:   zjl
#@File  :   4-2-1function.py

print(abs(-423))

# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
print(int('234'))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-3232323232))

# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串

print(hex(456))


print("--------定义函数")
# 定义函数
def my_abs(x):
    if(x>0):
        return x
    else:
        return -x
print(my_abs(-56))

def my_test(x):
    if(x>0):
        pass
    else:
        return -x

print(my_test(77))

# 改善my_abs() 因为上面的定义不够严格，没有类型判断
def my_abs1(x):
    if not isinstance(x,(float,int)):
        raise TypeError("not operand type")
    if x >= 0:
        return x
    else:
        return -x
print(my_abs1('11'))