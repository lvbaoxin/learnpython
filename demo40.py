import os.path

print(os.path.abspath("demo24.py"))  # F:\learnpython\demo24.py
print(os.path.join("e:\\learnpython", 'demo24.py'))  # F:\learnpython\demo24.py
print(os.path.splitext("demo24.py"))  # ('demo24', '.py')

# os.path模块操作目录相关函数
# abspath(path)用于获取文件或目录的绝对路径
# exists(path)用于判断文件是否存在，返回true或者false
# join(path,name) 将目录与目录或者文件名拼接起来
# splitext() 分离文件名和扩展名
# basename(path) 从一个目录中提取文件名
# dirname(path) 从一个路径中提供文件路径，不包括文件名
# isdir(path) 用于判断是否为路径
