list1 = [10,11,12,13,14,15,16,10]
list1.remove(10) #从列表中移除一个元素，如果有重复的元素只移除第一个元素。
print(list1) #[11, 12, 13, 14, 15, 16, 10]

list2 =[11,22,33,44,55,66]
list2.pop(1) #根据索引移除元素。
print(list2) #[11, 33, 44, 55, 66]

list3 = list1[1:4] #切片操作，删除至少一个元素，将产生一个新的列表对象。
print(list3)  #[12, 13, 14]


list4 =["a","b","c","d","e"]
list4.clear()  # 清空
print(list4) #[]

del list4 #删除
print(list4) # name 'list4' is not defined