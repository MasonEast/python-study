# 高阶函数：把一个函数作为其他函数的参数或返回值

def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2


old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]

# 内置函数sorted
"""
它可以实现对容器型数据类型（如：列表、字典等）元素的排序.
sorted函数从功能上来讲跟列表的sort方法没有区别，但它会返回排序后的列表对象，而不是直接修改原来的列表，
这一点我们称为函数的无副作用设计,也就是说调用函数除了产生返回值以外，不会对程序的状态或外部环境产生任何其他的影响
"""
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']

old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings, key=len) # 按长度排序
print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']


# 匿名函数 Lambda函数（只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]

import functools
import operator

# 用一行代码实现计算阶乘的函数
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(6))        # 720
print(is_prime(37))  # True


# 偏函数，指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数
"""
在 Python 语言中，我们可以使用functools模块的partial函数来创建偏函数。
例如，int函数在默认情况下可以将字符串视为十进制整数进行类型转换，
如果我们修修改它的base参数，就可以定义出三个新函数，分别用于将二进制、八进制、十六进制字符串转换为整数
"""
import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))    # 1001

print(int2('1001'))   # 9
print(int8('1001'))   # 513
print(int16('1001'))  # 4097