username = ['jack', 'tom', 'allen']
password = ['123123', '234234', '345345']


def reg():
    print("欢迎注册ATM系统")
    un = input('请输入您的用户名[注册]：')
    if un in username:
        print("您输入的用户名已经存在")
        return False
    else:
        pw = input("请输入您的密码[注册]")
        if len(pw) < 6:
            print("您输入的密码长度不足6位")
            return False
        else:
            username.append(un)
            password.append(pw)
            print("恭喜您注册成功！即将登录系统")
            return True


def login():
    un = input("请输入用户名[登录]")
    pw = input("请输入密码[登录]")
    if un in username:
        i = username.index(un)
        if password[i] == pw:
            print("恭喜您，登录成功")
        else:
            print("用户名或密码错误")
    else:
        print("用户名或密码错误")


if __name__ == '__main__':
    if reg():
        login()
