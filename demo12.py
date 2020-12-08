list1 = [11,22,33,44,55]
list1[1] = 14
print(list1)   #修改一个值。 [11, 14, 33, 44, 55]

list1[1:4] = [100,200,300]
print(list1) #修改多个值。 [11, 100, 200, 300, 55]


list2 =[2,3,6,1,8,32]
list2.sort() #升序 原列表
print(list2)#[1, 2, 3, 6, 8, 32]

list2.sort(reverse=True)  #降序 原列表
print(list2) #[32, 8, 6, 3, 2, 1]


list3 = [2,3,4,1,5,6]
new_list = sorted(list3)
print(new_list) #[1, 2, 3, 4, 5, 6] 产生新列表

desc_list = sorted(list3,reverse=True)
print(desc_list)  #[6, 5, 4, 3, 2, 1] 产生新列表