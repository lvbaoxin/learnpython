class Student:
    pass
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def eat(self):
        print(self.name + "在吃饭")

stu1 = Student("张三",20)
stu2 = Student("张二",30)
Student.eat(stu1) #张三在吃饭
stu2.gender = "女"
print(stu2.gender) #女
stu1.eat()#张三在吃饭