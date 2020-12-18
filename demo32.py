import pageage.moduleA as na  #na是pageage.moduleA这个模块的别名

print(na.a)
#使用import方式进行导入时，只能跟名包或模块名
from pageage import moduleA
from pageage.moduleA import a
#使用from .... import 可以导入包，模块，函数，变量。