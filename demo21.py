class Student:  # Student为类的名称，由一个或多个单词组成，每个单词的首字母大写，其余小写。
    pass
    native_pace = "吉林"  # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    # 在类之外称为函数，在类之内称为方法。

    def eat(self):
        print("学生在吃饭。")

    @staticmethod
    def mothed():
        print("静态方法")

    @classmethod
    def cm(cls):
        print("类方法，使用classmethod进行修饰")


print(Student.native_pace)  # 吉林

Student.cm()  # 类方法
Student.mothed()  # 静态方法
