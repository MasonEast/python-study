# 面向对象编程应用
"""
使用面向对象编程方法，首先需要从问题的需求中找到对象并抽象出对应的类，此外还要找到对象的属性和行为。
我们可以从需求的描述中找出名词和动词，名词通常就是对象或者是对象的属性，而动词通常是对象的行为。
类和类的关系可以粗略分为：继承，关联，依赖
"""

# 扑克游戏
"""
简单起见，我们的扑克只有52张牌（没有大小王），
游戏需要将52张牌发到4个玩家的手上，每个玩家手上有13张牌，
按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能。

分析功能：
  名词：玩家，扑克，牌。
    扑克和牌是关联关系，玩家和牌是关联还有依赖关系（手上有牌，出牌）
  牌的属性：花色，点数
  动词：发牌，出牌
"""

from enum import Enum
import random

class Suite(Enum):
  """花色 枚举"""
  SPADE, HEART, CLUB, DIAMOND = range(4) # 枚举是可迭代类型

class Card:
  """牌"""
  def __init__(self, suite, face):
    self.suite = suite
    self.face = face
  def __repr__(self):
    suites = '♠♥♣♦'
    faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回牌的花色和点数
  """
  运算符重载，Python 中要实现对<运算符的重载，需要在类中添加一个名为__lt__的魔术方法。
  很显然，魔术方法__lt__中的lt是英文单词“less than”的缩写，以此类推，
  魔术方法__gt__对应>运算符，魔术方法__le__对应<=运算符，__ge__对应>=运算符，__eq__对应==运算符，__ne__对应!=运算符。
  """
  def __lt__(self, other):
    if self.suite == other.suite:
      return self.face < other.face   # 花色相同比较点数的大小
    return self.suite.value < other.suite.value   # 花色不同比较花色对应的值
  
class Poker:
  """扑克"""
  def __init__(self):
    self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
    self.current = 0 # 记录发牌位置的属性
  def shuffle(self):
    """洗牌"""
    self.current = 0
    random.shuffle(self.cards)
  def deal(self):
    """发牌"""
    card = self.cards[self.current]
    self.current += 1
    return card
  @property
  def has_next(self):
    """判断还有没有牌"""
    return self.current < len(self.cards)
  
class Player:
  """玩家"""
  def __init__(self, name):
    self.name = name
    self.cards = [] # 玩家手上的牌
  def get_one(self, card):
    """摸牌"""
    self.cards.append(card)
  def arrange(self):
    """理牌"""
    self.cards.sort()

poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

for _ in range(13):
  for player in players:
    player.get_one(poker.deal())

for player in players:
  player.arrange()
  print(f'{player.name}: ', end='')
  print(player.cards)

"""
某公司有三种类型的员工，分别是部门经理、程序员和销售员。
需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
其中，部门经理的月薪是固定15000元；
程序员按工作时间（以小时为单位）支付月薪，每小时200元；
销售员的月薪由1800元底薪加上销售额5%的提成两部分构成。

分析：
  名词：员工，经理，程序员，销售，月薪

部门经理、程序员、销售员都是员工，有相同的属性和行为，那么我们可以先设计一个名为Employee的父类，
再通过继承的方式从这个父类派生出部门经理、程序员和销售员三个子类。
很显然，后续的代码不会创建Employee 类的对象，因为我们需要的是具体的员工对象，
所以这个类可以设计成专门用于继承的抽象类。Python 语言中没有定义抽象类的关键字，但是可以通过abc模块中名为ABCMeta 的元类来定义抽象类
"""

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
  """员工"""
  def __init__(self, name):
    self.name = name
  @abstractmethod # 对于暂时无法实现的方法，我们可以使用abstractmethod装饰器将其声明为抽象方法，所谓抽象方法就是只有声明没有实现的方法，声明这个方法是为了让子类去重写这个方法
  def get_salary(self):
    """结算月薪"""
    pass

class Manager(Employee):
  def get_salary(self):
    return 15000.0

class Programmer(Employee):
  def __init__(self, name, working_hour=0):
    super().__init__(name)
    self.working_hour = working_hour
  def get_salary(self):
    return 200 * self.working_hour
  
class Salesman(Employee):
  def __init__(self, name, sales=0):
    super().__init__(name)
    self.sales = sales
  def get_salary(self):
    return 1000 + self.sales * 0.05
  
emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    if isinstance(emp, Programmer): # isinstance函数来判断员工对象的类型
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')