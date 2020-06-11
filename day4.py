age = 18
s = '已经上'
# format是一个字符串中的函数
message = '乔治说：我今年{}岁了,{}幼儿园'.format(age,s)
print(message)


#name = input('请输入名字:') # 阻塞式
#print(name)
print('''
****************
     捕鱼达人
****************
    ''')
username = input("请输入您的用户名")
password = input("请输入您的密码")
print("%s,您好，请充值游戏币才可以进入游戏" %  username)
coins = input("请输入充值金额:")
print("%s充值成功，您的当前游戏币为%.0f" %(username,int(coins)))