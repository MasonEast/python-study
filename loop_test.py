# 100以内的素数

for num in range(2, 100):
  is_prime = True
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    print(num)

# 斐波那契

a, b= 0, 1
for _ in range(20):
  a, b = b, a + b # 表示将变量b的值赋给a，把a + b的值赋给b
  print(a)

# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

# 穷举法，也称为暴力搜索法
for x in range(0, 21):
  for y in range(0, 34):
    for z in range(0, 100, 3):
      if x + y + z == 100 and 5 *x + 3 * y + z // 3 == 100:
        print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

# 优化，三层变两层嵌套
for x in range(0, 21):
  for y in range(0, 34):
    z = 100 - x - y
    if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
       print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

# CRAPS赌博游戏
"""
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
为了增加代码的趣味性，我们设定游戏开始时玩家有1000元的赌注，
每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，
如果庄家获胜，玩家就会输掉自己下注的金额。游戏结束的条件是玩家破产（输光所有的赌注）。
"""

import random

money = 1000
count = 1
while money > 0:
  print(f'你的总资产为: {money}元')
  while True:
      debt = int(input('请下注: '))
      if 0 < debt <= money:
        break
  first_point = random.randrange(1, 7) + random.randrange(1, 7)
  print(f'\n玩家摇出了{first_point}点')
  if first_point == 7 or first_point == 11:
    money += debt
    print('玩家胜利!\n')
  elif first_point == 2 or first_point == 3 or first_point == 12:
    money -= debt
    print('庄家胜利!\n')
  else:
    while True:
      count += 1
      current_point = random.randrange(1, 7) + random.randrange(1, 7)
      print(f'\n玩家第一次摇出了{first_point}点，第{count}次摇出了{current_point}点')
      if current_point == 7:
        money -= debt
        count = 1
        print('庄家胜利!\n')
        break
      elif current_point == first_point:
        money -= debt
        count = 1
        print('玩家胜利!\n')
        break

print('您破产了，游戏结束！')