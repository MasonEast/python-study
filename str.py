# 转义字符要使用\

s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)
print(s2)

# 原始字符串（以r或R开头的字符串

s3 = '\it \is \time \to \read \now'
s4 = r'\it \is \time \to \read \now'
print(s3)
print(s4)

# 字符特殊表示（在\后面还可以跟一个八进制或者十六进制数来表示字符

s5 = '\141\142\143\x61\x62\x63'
s6 = '\u9a86\u660a' # \u后面跟 Unicode 字符编码
print(s5)
print(s6)

# 字符拼接和重复 + 和 *
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!

# 字符比较（字符串在计算机内存中也是以二进制形式存在的，那么字符串的大小比较比的是每个字符对应的编码的大小
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '骆昊'
print(ord('骆'))            # 39558
print(ord('昊'))            # 26122
s4 = '王大锤'
print(ord('王'))            # 29579
print(ord('大'))            # 22823
print(ord('锤'))            # 38180
print(s3 >= s4)             # True
print(s3 != s4)             # True

# 成员运算 in 和 not in
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)      # True
print('wo' not in s2)  # False
print(s2 in s1)        # False

# 获取字符串长度len方法
s = 'hello, world'
print(len(s))                 # 12
print(len('goodbye, world'))  # 14

# 索引和切片（字符串是不可变类型，无法通过索引修改字符串
s = 'abc123456'
n = len(s)
print(s[0], s[-n])    # a a
print(s[n-1], s[-1])  # 6 6
print(s[2], s[-7])    # c c
print(s[5], s[-4])    # 3 3
print(s[2:5])         # c12
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba

# 字符遍历 for in

s = 'hello'
for i in range(len(s)):
    print(s[i])

s = 'hello'
for elem in s:
    print(elem)

"""
字符串方法：
  capitalize: 首字母大写
  title: 每个单词首字母大写
  upper: 字符串都大写
  lower: 字符串都小写

  find: 正向查找字符串，并返回索引
  index: 和find类似
  rfind, rindex: 逆向查找

  startswith, endswith: 判断字符串是否以某个字符串开头和结尾
  is开头的方法判断字符串特征

  center, ljust, rjust: 格式化字符串，居中，左对齐，右对齐
  zfill: 字符串左侧补零

  strip, lstrip, rstrip: 获得将原字符串修剪掉左右两端指定字符之后的字符串，默认是修剪空格字符
  replace: 用新的内容替换字符串中指定的内容
  split, join: 拆分与合并（拆分成列表，从列表合并成字符串）

  encode, decode: 编解码，字符串编解码为字节串
"""

s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
print(s.index('or', 9))  # ValueError: substring not found

s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False 判断字符串是不是完全由数字构成
print(s2.isalpha())  # False 判断字符串是不是完全由字母构成
print(s2.isalnum())  # True 判断字符串是不是由字母和数字构成

s = 'hello, world'
print(s.center(20, '*'))  # ****hello, world****
print(s.rjust(20))        #         hello, world
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033

s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界

s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world

s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print('~'.join(words))  # I~love~you

# split方法默认使用空格进行拆分，我们也可以指定其他的字符来拆分字符串，而且还可以指定最大拆分次数来控制拆分的效果
s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 2)
print(words)  # ['I', 'love', 'you#so#much']

a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'\xe9\xaa\x86\xe6\x98\x8a'
print(c)                  # b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))  # 骆昊
print(c.decode('gbk'))    # 骆昊

# print格式化

a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}') # 3.6版本之后


# 匹配检查（正则，re模块
