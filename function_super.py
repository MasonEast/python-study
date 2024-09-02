# 装饰器： 用一个函数装饰另外一个函数并为其提供额外的能力
"""
装饰器本身是一个函数，它的参数是被装饰的函数，它的返回值是一个带有装饰功能的函数
装饰器是一个高阶函数，它的参数和返回值都是函数。
"""
# 装饰器的架子，wrapper函数就是用来给被传入的函数提供额外能力的
def record_time(func):
    
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        
        return result
    
    return wrapper

import time


def record_time(func):

    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result
    
    return wrapper

# 装饰器语法糖 @

import random
import time


def record_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

# 可去除装饰器函数的写法

import random
import time

from functools import wraps


def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# 调用装饰后的函数会记录执行时间
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')


# 递归调用：函数自己调用自己
"""
递归如果不能迅速收敛，很可能会引发栈溢出错误，从而导致程序的崩溃。
"""

def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)