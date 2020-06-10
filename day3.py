person = "娜娜"
address = "大连市沙河口区"
phone = "15999999999"
# ‘+’ 拼接，字符串 + 字符串是OK的 , 字符串 + int TypeError
print("订单的收件人是：" + person + ",收货地址是：" + address + ",联系方式："+phone)
# %s占位符 
print('订单的收件人是：%s,收货地址是：%s,联系方式：%s' %(person,address,phone))


age = 15
#can only concatenate str (not "int") to str
# str()强制类型的转换
print("年龄是" + str(age))  

isMarry = False
print("结婚否？回答：%s" % isMarry)  # 结婚否？回答：False

# %f 小数点后面的位数 而且是四舍五入
salary = 8899.28
print('薪水是：%.1f' % salary) #薪水是：8899.3
