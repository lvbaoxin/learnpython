# for else 适用于for执行完或者没有循环数据时，需要做的事情。
# num = int(input("请输入数量"))
# name = "张三"
# for i in range(num):
#     print("{}很饿，正在吃第{}馒头".format(name,i))
# else:
#     print("还没有给我馒头，{}饿哭了".format(name))

# #pass 空语句 只要有缩进而缩进的内容还不确定的时候，此是为了保证语法的正确性，就可以使用pass点位。不会报语法错误。    
# if 10 > 6:
#     print("10是大的")
# else:
#     pass

for i in range(3):
    username = input("请输入用户名")
    password = input("请输入密码")
    if username == "admin" and password == "123456":
        print("欢迎您：{}登录成功".format(username))
        break
    else:
        print("用户名或密码错误，请重新输入。")
