class Student:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def __str__(self):
        return "我的名字是{0},今年{1}岁".format(self.name,self.age)
stu = Student("张三","30")
print(stu)  #我的名字是张三,今年30岁  默认调用__str__方法