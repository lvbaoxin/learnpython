#打印3行4列，双循环。
# for i in range(1,4):
#     for j in range(1,5):
#         print("*", end="\t")
#     print("")

#打印9*9乘法表
for i in range(1,9):
    for j in range(1,i+1):
         print(j,"*",i,"=", i*j ,end="\t")
    print("")
