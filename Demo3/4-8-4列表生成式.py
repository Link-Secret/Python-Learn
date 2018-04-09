#@Time  :   2018/4/8 20:26
#@Author:   zjl
#@File  :   4-8-4列表生成式.py

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11)) 第二个参数为STOP
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环

L = []
for x in range(1,11):
    L.append(x*x)

print(L)

# 方法二：列表生成式
print([x*x for x in range(1,11)])


# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
# 过滤非字符串
L2 = [x for x in L1 if isinstance(x,str)]
# 小写
L2 = [s.lower() for s in L2]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')