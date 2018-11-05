# author: chenjie
# date: 2018/11/4

# 生成器都是迭代器，迭代器不一定是生成器
# list, tuple, dict, string: Iterable(可迭代对象)

list = [1, 2, 3, 4]

print(iter(list))       # <list_iterator object at 0x105361550>

# 什么是迭代器？
# 满足两个条件： 1. 有iter方法 2. 有next方法


# for 循环内部三件事：
# 1. 调用可迭代对象的iter方法返回一个迭代器对象
# 2. 不断调用迭代器对象的next方法
# 3. 处理StopIteration异常
