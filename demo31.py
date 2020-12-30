# 在python中一个扩展名为.py的文件不是一个模块

# 好处
# 一个模块中可以包含N多个函数
# 方便其它程序和脚本的导入并使用
# 避免函数名和变量名冲突
# 提高代码的可维护性
# 提高代码的可重用性
import math

print(math.pi)  # 3.141592653589793
print(dir(math))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf',
# 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau',
# 'trunc']

from math import pi

print(pi)  # 3.141592653589793
