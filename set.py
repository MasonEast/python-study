# 集合
"""
集合需要满足以下特性：
  无序性：一个集合中，每个元素的地位都是相同的，元素之间是无序的。
  互异性：一个集合中，任何两个元素都是不相同的，即元素在集合中只能出现一次。
  确定性：给定一个集合和一个任意元素，该元素要么属这个集合，要么不属于这个集合，二者必居其一，不允许有模棱两可的情况出现。

集合不支持索引运算，不能有重复元素，运算性能优于列表运算

集合底层使用了hash存储(散列存储)，所以集合中只能存储hashable类型的元素
  通常不可变类型都是hashable类型，如整数（int）、浮点小数（float）、布尔值（bool）、字符串（str）、元组（tuple）等。
  可变类型都不是hashable类型，因为可变类型无法计算出确定的哈希码，所以它们不能放到集合中。
  例如：我们不能将列表作为集合中的元素；同理，由于集合本身也是可变类型，所以集合也不能作为集合中的元素。
  我们可以创建出嵌套的列表，但是我们不能创建出嵌套的集合，这一点在使用集合的时候一定要引起注意。
"""

# 创建集合

set1 = {1, 2, 3, 3, 3, 2} # {}字面量创建，至少有一个元素，否则会当成空字典
print(set1)

set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'} # 会过滤重复的
print(set2)

set3 = set('hello') #转换其他类型序列
print(set3)

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

# 集合的遍历
set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for elem in set1:
    print(elem) # 集合的无序性

# 成员运算 in 和 not in

set1 = {11, 12, 13, 14, 15}
print(10 in set1)      # False 
print(15 in set1)      # True
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True

# 二元运算：交集，并集，差集，对称差等

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}

# 并集
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
print(set1 - set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}

# 对称差
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}

set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
# set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
set1 &= set3
# set1.intersection_update(set3)
print(set1)  # {3, 6}
set2 -= set1
# set2.difference_update(set1)
print(set2)  # {2, 4}

# 比较运算 == 和 !=，还有真子集，子集，超集<、<=、>、>=
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

print(set1 < set2)   # True
print(set1 <= set2)  # True
print(set2 < set3)   # False
print(set2 <= set3)  # True
print(set2 > set1)   # True
print(set2 == set3)  # True

print(set1.issubset(set2))    # True 判断子集
print(set2.issuperset(set1))  # True 判断超集

"""
集合的方法
  集合是可变类型，可以添加或删除元素
  add
  discard, remove: 删除元素
  clear
  pop: 随机删除一个元素并返回

  isdisjoint: 判断两个集合有没有相同的元素

  frozenset: 不可变类型的集合（不能删除和添加），元素可以计算出哈希码，所以它可以作为set的元素
"""
set1 = {1, 10, 100}

# 添加元素
set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}

# 清空元素
set1.clear()
print(set1)  # set()

set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True

fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False