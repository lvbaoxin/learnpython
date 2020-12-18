import os

path = os.getcwd()
lis = os.listdir(path)
for filename in lis:
    if filename.endswith(".py"):
        print(filename)
