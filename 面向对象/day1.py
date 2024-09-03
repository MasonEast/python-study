"""
面向对象编程：
  把一组数据和处理数据的方法组成对象，把行为相同的对象归纳为类，通过封装隐藏对象的内部细节，
  通过继承实现类的特化和泛化，通过多态实现基于对象类型的动态分派。

在面向对象编程中，类是一个抽象的概念，对象是一个具体的概念。
一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类
"""

# 定义类
class Student:
  def __init__(self, name, age): # 自动执行__init__方法，完成对内存的初始化操作，也就是把数据放到内存空间中。所以我们可以通过给Student类添加__init__方法的方式为学生对象指定属性，同时完成对属性赋初始值的操作
    self.name = name
    self.age = age
  def study(self, course_name):
    print(f'{self.name}同学正在学习{course_name}')
  def play(self):
    print(f'{self.name}同学正在玩游戏.')

stu1 = Student('a', 14)
stu2 = Student('b', 15)
print(stu1)    # <__main__.Student object at 0x10ad5ac50>
print(stu2)    # <__main__.Student object at 0x10ad5acd0> 
print(hex(id(stu1)), hex(id(stu2)))    # 0x10ad5ac50 0x10ad5acd0
# 我们定义的变量其实保存的是一个对象在内存中的逻辑地址（位置），通过这个逻辑地址，我们就可以在内存中找到这个对象

Student.study(stu1, '数学')
stu1.study('数学')
stu2.play()

# 面向对象编程的三大核心
"""
封装: 隐藏一切可以隐藏的实现细节，只向外界暴露简单的调用接口
继承
多态
"""

# example：时钟
import time

class Clock:
  def __init__(self, h=0, m=0, s=0):
    self.h = h
    self.m = m
    self.s = s
  def run(self):
    self.s += 1
    if self.s == 60:
      self.s = 0
      self.m += 1
      if self.m == 60:
        self.m = 0
        self.h += 1
        if self.h == 24:
          self.h = 0
  def show(self):
    return f'{self.h:0>2d}:{self.m:0>2d}:{self.s:0>2d}'
  
clock = Clock(23, 59, 57)
# while True:
#   print(clock.show())
#   time.sleep(1)
#   clock.run()

# 可见性和属性装饰器：可以通过给对象属性名添加前缀下划线的方式来说明属性的访问可见性，例如，可以用__name表示一个私有属性

class Student2:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student2('王大锤', 20)
stu.study('Python程序设计')
print(stu._Student2__name) # python中的私有属性不是绝对访问不到，前面加类名也是可以访问到的
print(stu.__name)  # AttributeError: 'Student' object has no attribute '__name'

# 动态属性：Python 语言属于动态语言

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
stu.sex = '男'  # 给学生对象动态添加sex属性

# 不希望在使用对象时动态的为对象添加属性，可以使用 Python 语言中的__slots__魔法
class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'

# 静态方法和类方法

"""
对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，
区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。
静态方法通常也可以直接写成一个独立的函数，因为它并没有跟特定的对象绑定。
"""

# 可以给上面计算三角形周长和面积的方法添加一个property装饰器（Python 内置类型），这样三角形类的perimeter和area就变成了两个属性，不再通过调用方法的方式来访问，而是用对象访问属性的方式直接获得

class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t = Triangle(3, 4, 5)
print(f'周长: {t.perimeter}')
print(f'面积: {t.area}')

# 继承和多态

class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""
    
    def __init__(self, name, age):
        super().__init__(name, age) # 通过super().__init__()来调用父类初始化方法
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')