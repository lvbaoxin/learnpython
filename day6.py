#三目表达式
#python 的格式 ： 结果 if 表达式 else 结果
a=5
b=6
result = (a+b) if a > b else (b-a)
'''
判断表达式是true 还是false
如果是True 将if前面的内容进行运算，并将结果赋值成result
如果是False则将else后面的内容运算结果，并将结果赋值成result
'''
print(result)

#运算符的优先级：
'''
    排序：
    **
    ~
    + - （符号运算符）
    * / // %
    + - (加减)
    << >>
    & 
    ^
    |
    ==  != < <=  > >=
    is is not
    not
    and 
    or 

'''
username = 'admin'
if username != '':
    print("登录成功")




age = int(input("请输入年龄"))
username = input("请输入用户名")
if age > 18 and username != "":
    print("{}今年{}岁".format(username,age))


for i in range(3):
     print("hello world")


         