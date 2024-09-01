# 元组，元组和列表不同之处在于，元组是不可变类型
"""
元组方法:
  len: 查看元组中元素数量
"""

# 定义元组
t1 = (33, 21, 45)
t2 = ('aa', 33, True)

print(type(t1), type(t2))
print(len(t1), t1[0], t2[-1])

# 切片运算
print(t2[:2]) # 'aa', 33
print(t2[::2]) # 'aa', True

# 循环遍历元组中的元素
for elem in t1:
    print(elem)

# 成员运算
print(12 in t1)         # True
print(99 in t1)         # False
print('Hao' not in t2)  # False

# 拼接运算
t3 = t1 + t2
print(t3)  # (35, 12, 98, '骆昊', 43, True, '四川成都')

# 比较运算
print(t1 == t3)            # False
print(t1 >= t3)            # False
print(t1 <= (35, 11, 99))  # False

# ()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数

a = ()
print(type(a))  # <class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>


# 打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
# 解包操作
i, j, k = a
print(i, j, k)  # 1 10 100

# 解包一般是长度对应，但可以通过 * 变量接收多个值，* 只能出现一次

a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)        # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)        # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)        # [1, 10] 100 1000
*i, j = a
print(i, j)           # [1, 10, 100] 1000
i, *j = a
print(i, j)           # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)     # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)  # 1 10 100 1000 []

# 解包对所有序列都成立，如列表，range函数，字符串都可以

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

# 交换变量值

a, b = b, a
a, b, c = b, c, a

# 元组和列表比较

"""
1. 元组是不可变类型，更适合多线程环境，因为它降低了并发访问变量的同步化开销
2. 元组是不可变类型，在创建时间上优于对应的可变类型
"""

import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

# 元组和列表可以相互转换

infos = ('a', 43, True, '四川成都')
# 将元组转换成列表
print(list(infos))  # ['a', 43, True, '四川成都']

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')
