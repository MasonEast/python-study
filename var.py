# -*- coding: utf-8 -*-
"""
变量类型:
  整型int
  浮点型float
  字符串str
  布尔型bool
变量命名: 
  规则部分: 
    规则1: 变量名由字母、数字和下划线构成, 数字不能开头。需要说明的是, 这里说的字母指的是 Unicode 字符, Unicode 称为万国码, 囊括了世界上大部分的文字系统, 这也就意味着中文、日文、希腊字母等都可以作为变量名中的字符, 但是一些特殊字符（如: ！、@、#等）是不能出现在变量名中的。我们强烈建议大家把这里说的字母理解为尽可能只使用英文字母。
    规则2: Python 是大小写敏感的编程语言, 简单的说就是大写的A和小写的a是两个不同的变量, 这一条其实并不算规则, 而是需要大家注意的地方。
    规则3: 变量名不要跟 Python 的关键字重名, 尽可能避开 Python 的保留字。这里的关键字是指在 Python 程序中有特殊含义的单词（如: is、if、else、for、while、True、False等）, 保留字主要指 Python 语言内置函数、内置模块等的名字（如: int、print、input、str、math、os等）。
  惯例部分: 
    惯例1: 变量名通常使用小写英文字母, 多个单词用下划线进行连接。
    惯例2: 受保护的变量用单个下划线开头。
    惯例3: 私有的变量用两个下划线开头。
"""

a = 100
b = 100.1
c = 'hello'
d = True
e = '101'

print(type(a), type(b), type(c), type(d))

print(float(a))
print(int(e, base=2))   # str类型的'101'按二进制转成int，输出5
print(int(e))

print(bool(c))
print(chr(a))   # int类型的100转成str，输出'd'
print(ord('e')) # str类型的'e'转成int，输出101

print(0b100)