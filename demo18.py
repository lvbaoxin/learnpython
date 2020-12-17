def fun(num):
    odd=[]
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst = [10,11,12,13,14,15,15]
print(fun(lst))#([11, 13, 15, 15], [10, 12, 14])
#如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】 return 可以省略不写
#函数的返回值，如果是1个，直接返回类型
#函数的返回值，如果是多个，返回的结果为元组



