#@Time  :   2018/4/2 18:08
#@Author:   zjl
#@File  :   4-2-2导入math.py

import math

def move(x,y,step,angle=0):
    nx = x + step*math.sin(step)
    # y轴一般取向下，即第四象限
    ny = y - step*math.cos(step)
    return nx , '-' ,ny

# 即Python函数返回的是一个元组，tuple
# 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个
# 变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
m = move(100,100,600,math.pi/6)
print(m)

# 计算平方根的函数
def quadratic(a,b,c):
    x1 = (-b-math.sqrt(b*b-4*a*c))/2*a
    x2 = (-b+math.sqrt(b*b-4*a*c))/2*a
    return x1,x2
print(quadratic(3,-4,-2))

# n次方
def power(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s
print(power(2,3))


# 可以设置默认参数
def power1(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power1(2,0))

print("******")

# 定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=[]):
    L.append('end')
    return L
print(add_end())
print(add_end())
print(add_end())

# 因为默认参数L的值一开始为[]，可是调用后，就变成了['end'],此默认参数L的值为['end']

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
# 它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。


# 定义的时候定义不变的None为对象
# 默认参数L为None
def add_end1(L=None):
    if L is None:
        L = []
    L.append('end')
    return L
print(add_end1())
print(add_end1())
print(add_end1([1]))


print("******")

# 可变参数

# 折中方法,传入tump元组或者list
def calc(number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum
print(calc([0,1,2,3,4]))

# 真正的可变参数
# *number，传入随便的个数参数
#                          在函数内部，参数numbers接收到的是一个tuple
def calc1(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum
print(calc1(1,2,3,4))

print("******")

# 如果已经有一个list或者tuple，要调用一个可变参数
nums = [0,1,2]
print(calc1(nums[0],nums[1],nums[2]))
# 推荐下面写法
print(calc1(*nums))


# 关键字参数
# **kw是关键字参数，kw接收的是一个dict。
# 作用:可以扩展函数的功能
def people(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

people('mike',20)
people('mike2',21,num1='fun1',num2='fun2')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'n1':'1','n2':'2','n3':3}
people('mike3',22,**extra)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name,age,*,city,job):
    print("name:",name,"age:",age,city,job)
person("jack",22,city='shanghai',job='Python')


# 参数组合

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 练习
def couple(*args):
    s = 1
    for n in args:
        s = s * n;
    return s;
print(couple(1))
print(couple(1,2,3,5,10))


# 小结

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。