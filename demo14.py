#只包含一个元素的时候，需要加上 " , "
tuple1 = ("python","world",22)
print(tuple1) #元组的创建方式1  ('python', 'world', 22)

tuple2 = tuple(("hello",'world',11))
print(tuple2) #元组的创建方式2 使用内置函数tuple()   ('hello', 'world', 11)


tuple3 = ("abc",[10,20,30],33)
tuple3[1].append(100)
print(tuple3)  #('abc', [10, 20, 30, 100], 33)

for item in tuple3:
    print(item)  #遍历  abc  [10, 20, 30, 100]  33
