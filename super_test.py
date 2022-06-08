#test the function of super

class Student(object):
    """ 定义一个学生对象"""

    def __init__(self):
        print('name')
        print('age')

class Malestudent(Student):
    """ 定义一个男学生对象"""

    def __init__(self):
        print('.name')
        print('.age')

class Fmalestudent(Student):
    """ 定义一个女学生对象"""

    def __init__(self):
        super(Fmalestudent,self).__init__()

if __name__ == '__main__':
    A = Malestudent()
    B = Fmalestudent()