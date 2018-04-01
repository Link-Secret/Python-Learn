#@Time  :   2018/4/1 17:53
#@Author:   zjl
#@File  :   4-1-8dict和set.py

# dict相当于 map

# 要保证hash的正确性，作为key的对象就不能变
# 在Python中，字符串、整数等都是不可变的
# 因此，可以放心地作为key。而list是可变的，就不能作为key：