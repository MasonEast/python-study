# -*- coding: utf-8 -*-
# 循环结构

# for in循环
import time

"""
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。
"""
# for i in range(60): # i从0加到59循环
#   print(i)
#   time.sleep(1)

total = 0
for i in range(1, 101): # 计算1到100的整数求和
  total += i
print(total)

for i in range(2, 101, 2): # 计算1到100的偶数求和
  total += i
print(total)
print(sum(range(2, 101, 2))) # 更简单的方法，计算1到100的偶数求和

# 当不能确定循环次数，可以使用while循环

total = 0
i = 1
while i <= 100:  # 计算1到100的整数求和
  total += i
  i += 1
print(total)

# break和continue

while True:
    total += i
    i += 2
    if i > 100:
        break # break 用法
print(total) 

# 嵌套

for i in range(1, 10):
   for j in range(1, i + 1):
      print(f'{i}x{j} = {i * j}', end='\t')
   print()

# 猜数字小游戏

import random

answer = random.randrange(1,101)
counter = 0
while True:
   counter += 1
   num = int(input('请输入: '))
   if num > answer:
      print('大了点')
      continue
   elif num < answer:
      print('小了点')
   else:
      print('您猜对了！')
      break
print(f'您一共猜了{counter}次！')
