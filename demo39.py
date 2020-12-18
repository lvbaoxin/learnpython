import os

os.system("notepad.exe")  # 打开记事本
os.startfile("D:\\Program Files (x86)\\Tencent\\QQ\Bin\\QQScLauncher.exe")  # 打开QQ
print(os.getcwd())  # F:\learnpython

# getcwd() 返回当前的工作目录
# listdir(path)  返回指定路径下的文件和目录信息
# mkdir(path[,mode]) 创建目录
# makedirs(path/path2...[,mode])创建多级目录
# rmdir(path) 删除目录
# removedirs(path1/path2...)删除多级目录
# chdir(path) 将path设置为当前工作目录
