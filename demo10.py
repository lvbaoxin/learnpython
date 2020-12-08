list1 = ["hello","world",23,"hello"]
print(list1.index("hello"))#查找索引位置
print(list1.index("hello",1,4)) #查找索引1开始到3结束的位置。

list2 = [10,11,12,13,14,15,16,17,18]
print(list2[1:6:1]) #切出新列表  start = 1;stop=6;step=1;

list3 = [11,22,33,44,55]
print(10 in list3) #false
print(10 not in list3) #true
for item in list3: #遍历
    print(item)

list4=[1,2,3,4,5,6]
list4.append(7) #末尾添加一个新元素
list5 = [8,9,10]
list4.extend(list5) #在末尾添加至少一个新元素
print(list4)

list6 = [11,22,33,44,55,66]
list6.insert(1,90) #在任意位置添加一个新元素
print(list6)