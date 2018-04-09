#@Time  :   2018/4/9 9:34
#@Author:   zjl
#@File  :   4-9-1生成器.py

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator

# 第一种办法 把一个列表生成式的[]改成()，就创建了一个generator

L = [ x * x for x in range(1,11)]
print(L)

g = (x * x for x in range(1,11))

print(next(g))

for i in g:
    print(i,end=', ')
print()

# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b,end=', ')
        a,b = b,a+b
        n = n + 1
    return 'done'

fib(5,)
print()

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，
# 可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator：

# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fibY(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

f = fibY(5)

for i in f:
    print(i,end=', ')


    # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

#     最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行


# 练习

# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：
#
# # -*- coding: utf-8 -*-

def triangles1():
    L = [1]
    while True:
        yield L
        L = [x+y for x, y in zip([0]+L, L+[0])]


# 第二种
def triangles():
    L = [1]
    while True:
        yield L
        # 在L后面添加[1]
        L = L + [1]
        # L1为中间量，相当于当前L的复制，且多一个[1]
        L1 = L.copy()
        # 基于L1，改变L的值
        for x in range(1,len(L1)-1):
            L[x] = L1[x-1]+L1[x]



    # 期待输出:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
    # [1, 6, 15, 20, 15, 6, 1]
    # [1, 7, 21, 35, 35, 21, 7, 1]
    # [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')