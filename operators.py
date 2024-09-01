# -*- coding: utf-8 -*-

print(321 + 12)     # 加法运算，输出333
print(321 - 12)     # 减法运算，输出309
print(321 * 12)     # 乘法运算，输出3852
print(321 / 12)     # 除法运算，输出26.75
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241

a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 15 * 13

"""
比较运算符
比较运算符的优先级高于赋值运算符，所以flag0 = 1 == 1先做1 == 1产生布尔值True，再将这个值赋值给变量flag0。
print函数可以输出多个值，多个值之间可以用,进行分隔，输出的内容默认以空格分开。
"""

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8

#对print函数输出的内容进行了格式化处理，print输出的字符串中有两个%.1f占位符，这两个占位符会被%之后的(f, c)中的两个float类型的变量值给替换掉，浮点数小数点后保留1位有效数字。如果字符串中有%d占位符，那么我们会用int类型的值替换掉它，如果字符串中有%s占位符，那么它会被str类型的值替换掉。
# print('%.1f华氏度 = %.1f摄氏度' % (f, c)) 

import math

radius = float(input('请输入圆的半径: '))  # 输入: 5.5
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2

# py3.8新加输出方法
print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
print(f'{area = :.2f}')       # 输出：area = 95.03