def fun(arg1,arg2):
    print("arg1=" ,arg1)
    print("arg2=",arg2)
    arg1 = 100
    arg2.append(10)
    print("arg1=" ,arg1)
    print("arg2=",arg2)

n1 = 11
n2=[22,33,44]
print(n1)
print(n2)
fun(n1,n2)
print(n1)
print(n2)
# 11
# [22, 33, 44]
# arg1= 11
# arg2= [22, 33, 44]
# arg1= 100
# arg2= [22, 33, 44, 10]
# 11
# [22, 33, 44, 10]