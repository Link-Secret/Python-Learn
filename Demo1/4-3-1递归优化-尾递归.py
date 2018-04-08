#@Time  :   2018/4/3 9:05
#@Author:   zjl
#@File  :   4-4-1递归优化-尾递归.py


# 一般递归
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)*n

print(fact(4))

# 循环    理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
def fact1(n):
    s = 1
    while n > 1:
        s = s * n
        n -= 1
    return s

print(fact1(4))


# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况

def fact2(n):
	return fact_item(n,1)

def fact_item(num,result):
	if num == 1:
		return result
	return fact_item(num-1,num*result)

print(fact2(5))

# 优化fact(5)对应的fact_iter(5, 1)的调用如下：

# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

# 遗憾的是，大多数编程语言没有针对尾递归做优化，
# Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

