class Car:
    def __init__(self, brand):
      self.brand = brand
    def start(self):
        print("汽车启动")

car = Car("大众")
car.start()#汽车启动
print(car.brand)#大众


class Student:
    def __init__(self, name, age):
      self.name = name
      self.__age = age  #年龄不希望在类的外部被使用
    def show(self):
        print(self.name,self.__age)

stu=Student("张三",30)
stu.show()
#print(stu.__age)#'Student' object has no attribute '__age'
#print(dir(stu))
#['_Student__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'show']
print(stu._Student__age)  #30