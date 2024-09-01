items = ['a', 'a']
items.clear()
print(len(items))

"""
双色球每注投注号码由6个红色球和1个蓝色球组成。红色球号码从1到33中选择，蓝色球号码从1到16中选择。每注需要选择6个红色球号码和1个蓝色球号码
"""
import random

red_balls = list(range(1, 34))
selected_balls = []
for _ in range(6):
  index = random.randrange(len(red_balls))
  selected_balls.append(red_balls.pop(index))

selected_balls.sort()

for ball in selected_balls:
  print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

blue_ball = random.randrange(1, 17)
print(f'\033[034m{blue_ball:0>2d}\033[0m')

# 利用random模块提供的sample和choice函数来简化上面的代码

red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
# 从红色球列表中随机抽出6个红色球（无放回抽样）
selected_balls = random.sample(red_balls, 6)
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 从蓝色球列表中随机抽出1个蓝色球
blue_ball = random.choice(blue_balls)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')