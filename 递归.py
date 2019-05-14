# -*- coding: utf-8 -*-
# date: 2018/10/28

# 关于递归的特点？
# 1.自己调用自己
# 2.必须要有结束条件

# 但凡是递归可以写的程序，循环都可以解决
# 递归的效率在很多时候会很低


# 阶层
# 5 != 5 * 4 * 3 * 2 * 1 = 120

# 方法1
# def fact(n):
#     ret = 1
#     for i in range(1, n + 1):
#         ret = ret * i
#     return ret
#
# print(fact(5))    # 120

# 方法2（递归）
def fact(n):
    if  n == 1:
        return  1
    return n * fact(n - 1)

print(fact(5))


# 斐波那契

def feibo(n):
    if n <= 1:
        return n
    return feibo(n - 1) + feibo(n - 2)

print(feibo(8))


# 内置函数
# http://www.cnblogs.com/yuanchenqi/articles/5828233.html

# 重要内置函数

str = ['a', 'b', 'c', 'd']

# filter 过滤

def fun1(s):
    if s != 'a':
        return s

ret =  filter(fun1, str)

print(ret)   # <filter object at 0x10e2586a0> ret是一个迭代器对象
print(list(ret))    # ['b', 'c', 'd']

# map
def fun2(s):
    return s + 'hello'

ret = map(fun2, str)

print(ret)       # <map object at 0x108ec0d30>
print(list(ret))    # ['ahello', 'bhello', 'chello', 'dhello']

# reduce

from functools import reduce

def add1(x, y):
    return x + y

print(reduce(add1, range(1 ,101)))  # 5050 reduce 的结果就是一个值

# lambda（匿名函数）
lambda a, b : a + b

print(reduce(lambda x, y : x * y, range(1, 9)))



# test fix
