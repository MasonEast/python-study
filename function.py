# 使用def关键字来定义函数（如果函数中没有return语句，那么函数会返回代表空值的None), 函数是对功能相对独立且会重复使用的代码的封装

def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))

# 导入函数
from math import factorial
# as可以设置别名 from math import factorial as f

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))

# 函数参数
def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b

print(make_judgement(b=2, c=3, a=1))  # False 带默认值的参数必须放在不带默认值的参数之后
print(make_judgement(c=6, b=4, a=5))  # True

# /前面的参数是强制位置参数， 3.8版本
def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
# 下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
# print(make_judgement(b=2, c=3, a=1))


# *后面的参数是命名关键字参数
def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
# 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
# TypeError: make_judgement() takes 0 positional arguments but 3 were given
# print(make_judgement(1, 2, 3))


# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45

# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)


# 模块管理函数
"""
Python 中每个文件就代表了一个模块（module），
我们在不同的模块中可以有同名的函数，
在使用函数的时候，我们通过import关键字导入指定的模块再使用完全限定名（模块名.函数名）的调用方式，就可以区分到底要使用的是哪个模块中的函数
"""

import module1 as m1
import module2 as m2

m1.foo()  # hello, world!
m2.foo()  # goodbye, world!

from module1 import foo as f1
from module2 import foo as f2

f1()  # hello, world!
f2()  # goodbye, world!

# 部分内置函数(不需要import即可使用)

"""
abs	返回一个数的绝对值，例如：abs(-1.3)会返回1.3。
bin	把一个整数转换成以'0b'开头的二进制字符串，例如：bin(123)会返回'0b1111011'。
chr	将Unicode编码转换成对应的字符，例如：chr(8364)会返回'€'。
hex	将一个整数转换成以'0x'开头的十六进制字符串，例如：hex(123)会返回'0x7b'。
input	从输入中读取一行，返回读到的字符串。
len	获取字符串、列表等的长度。
max	返回多个参数或一个可迭代对象中的最大值，例如：max(12, 95, 37)会返回95。
min	返回多个参数或一个可迭代对象中的最小值，例如：min(12, 95, 37)会返回12。
oct	把一个整数转换成以'0o'开头的八进制字符串，例如：oct(123)会返回'0o173'。
open	打开一个文件并返回文件对象。
ord	将字符转换成对应的Unicode编码，例如：ord('€')会返回8364。
pow	求幂运算，例如：pow(2, 3)会返回8；pow(2, 0.5)会返回1.4142135623730951。
print	打印输出。
range	构造一个范围序列，例如：range(100)会产生0到99的整数序列。
round	按照指定的精度对数值进行四舍五入，例如：round(1.23456, 4)会返回1.2346。
sum	对一个序列中的项从左到右进行求和运算，例如：sum(range(1, 101))会返回5050。
type	返回对象的类型，例如：type(10)会返回int；而 type('hello')会返回str。
all  如果传入的序列中所有的布尔值都是True，all函数返回True，否则all函数返回False。
"""