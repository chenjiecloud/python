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

