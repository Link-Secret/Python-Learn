#@Time  :   2018/4/3 10:19
#@Author:   zjl
#@File  :   4-3-2.py

# 汉诺塔
def move(n, a, b, c):
    if n==1:
        print(a+"--->"+c)
    else:
        # 先，n-1个到b
        # 最后，最大的到c当基座
        # 第二步，最后一个到c
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

# 函数如果没return，则默认返回None
move(5,"A","B","C")