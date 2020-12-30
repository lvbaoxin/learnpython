class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值
cpu1 = Cpu()
cpu2 = cpu1
print(cpu1)  # <__main__.Cpu object at 0x0000024D406B7C10>
print(cpu1)  # <__main__.Cpu object at 0x0000024D406B7C10>
# 类的浅拷贝
import copy

disk = Disk()
computer = Computer(cpu1, disk)
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
# <__main__.Computer object at 0x000001F102E82130> <__main__.Cpu object at 0x000001F102EB7C10> <__main__.Disk object at 0x000001F102E82880>
print(computer2, computer2.cpu, computer2.disk)
# <__main__.Computer object at 0x000001F102EF15E0> <__main__.Cpu object at 0x000001F102EB7C10> <__main__.Disk object at 0x000001F102E82880>

# 类的深拷贝
computer3 = copy.deepcopy(computer)
print(computer3, computer3.cpu, computer3.disk)
# <__main__.Computer object at 0x00000234F5DD1940> <__main__.Cpu object at 0x00000234F5E0D7F0> <__main__.Disk object at 0x00000234F5E0D850>

# 变量的贬值操作
# 只是形成两个变量，实际上还是指向同一个对象

# 浅拷贝
# python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象

# 深拷贝
# 使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同。
