class Student:
    def __init__(self, name, age, stuno):
        self.name = name
        self.age = age
        self.stuno = stuno

    def study(self):
        print("我正常学习")


if __name__ == '__main__':
    student = Student('jack', 23, 's022')
    student.study()
    print(student.name)
