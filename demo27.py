class Animal(object):
   def eat(self):
       print("动物会吃")

class Dog(Animal):
    def eat(self):
        print("狗会吃骨头")
class Cat(Animal):
    def eat(self):
        print("猫会吃鱼")
class Person:
    def eat(self):
        print("人吃五谷杂粮")

def fun(obj):
    obj.eat()

fun(Dog())#狗会吃骨头
fun(Cat())#猫会吃鱼
fun(Animal())#动物会吃
fun(Person())#人吃五谷杂粮

