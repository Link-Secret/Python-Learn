#@Time  :   2018/4/1 13:53
#@Author:   zjl
#@File  :   String.py

print("\\\t\\")

# r'' 表示''里面的内容不转义
print(r'\\\\')

# '''  多行内容 '''
print('''line1
    line2
line3''')

print("-----------")

# 还可以加r
print(r'''line1
    line2
line3''')

print("---------------------")

# python 里面空值为none
# 动态语言，赋值的时候不用关心类型
a = 123
print(a)
a = '字符串'
print(a)

# b得到的是a指向的字符串的在内存中的地址
print("------")
a = "123"
b = a
a = "改变值"
print(b)

# 除法分两种
# / 结果一定为浮点数
# // 地除法，结果只取得整数部分

print("*********************小结")
# 小结：
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)


# python 整数型没有大小限制 浮点数也没有限制，但超出一定范围用INF（无限大）表示

print("----编码问题")

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'bytes'
print(x)
# 指定编码
print('中文'.encode("utf-8"))

# bytes 转换成ASCII编码
print(x.decode('ascii'))