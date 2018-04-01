#@Time  :   2018/4/1 17:21
#@Author:   zjl
#@File  :   4-1-6条件判断.py

birth = input('birth:')
# birth接收的是str类型
birth = int(birth)
if birth < 2000:
    print("00前")
else:
    print("00后")



h = input('height:')
w = input('weight:')
height = float(h)
weight = float(w)
bmi = w / h / h
if bmi < 18.8:
    b = '过轻'
elif 18.5 <= bmi <= 25:
    b = '正常'
elif 25 <= bmi <= 32:
    b = '肥胖'
elif bmi > 32:
    b = '严重肥胖'
print('小明的BMI指数是:%s' % b)