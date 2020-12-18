with open('a.txt', 'r', encoding="utf") as file:
    print(file.read())


class MyContent(object):
    def __enter__(self):
        print("enter方法被调用执行")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被调用执行")

    def show(self):
        print("show方法被调用执行")


with MyContent() as file:
    file.show()
# enter方法被调用执行
# show方法被调用执行
# exit方法被调用执行

with open('1.jpg', 'rb') as img_src:
    with open('copy2.jpg', 'wb') as copy_src:
        copy_src.write(img_src.read())
