class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self, name):
      self.name = name
x = C("jack")
print(x.__dict__) #实例对象的属性字典 {'name': 'jack'}
print(x.__class__) #实例对象的所属的类 <class '__main__.C'>
print(C.__bases__) #C类的父类的元素 (<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)#  类的基类     <class '__main__.A'>
print(C.__mro__)#类的层次结构  (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(A.__subclasses__()) #子类的列表