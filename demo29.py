class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student("张三")
stu2 = Student("李四")
stu3 = stu1 + stu2
print(stu3)  # 张三李四 实现了两个对象的加法运算，因为在Student类中，编写了__add__()方法

lst = [11, 22, 33, 44]
print(len(lst))  # 4
print(lst.__len__())  # 4
print(len(stu1))  # 2
