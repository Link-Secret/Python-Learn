class Student(object):
    count = 0
    """docstring for Student"""

    def __init__(self, name):
        super(Student, self).__init__()
        self.name = name
        Student.count = Student.count + 1


if __name__ == '__main__':
    # st1 = Student('st1')
    # st2 = Student('st2')
    # print(Student.count)

    if Student.count != 0:
        print('测试失败')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('测试失败!')
        else:
            lisa = Student('Bart')
            if Student.count != 2:
                print('测试失败!')
            else:
                print('Students:', Student.count)
                print('测试通过!')
