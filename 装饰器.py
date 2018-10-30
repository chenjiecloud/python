# author: chenjie
# date: 2018/10/29

# 1.函数的作用域：L-E-G-B
x = 10 # 全局作用域 global

def f():
    t = 5   # 嵌套作用域 enclosing
    def inner():
        count = 7   # 局部作用域 lcoal
        return 1

# 2.高阶函数
# 函数名可以作为参数输入
# 函数名可以作为返回值

# 3.闭包
# 定义：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）

def outer():
    x = 10
    def inners():   # 条件一 inners 就是内部函数
        print(x)    # 条件二 外部环境的一个变量
    return inners   # 结论 内部函数 inners 就是一个闭包

outer() ()

# f = outer()     # <function outer.<locals>.inners at 0x10a5feae8>
# f()

# 关于闭包: 闭包 = 函数 + 定义函数时的环境

# inners() 局部变量，全局无法调用


# 装饰器（函数）

# 开放封闭原则

# 开放：对扩展开放
# 封闭：对修改封闭

import time

def show_time(func):
    def inner1():
        start = time.time()
        func()
        end = time.time()
        print('spend: %s' % (end - start))
    return inner1


@show_time  # foo = show_time(foo)
def foo():
    print('foo....')
    time.sleep(2)

foo()


# 功能函数加参数
def show_spend_time(func):
    def inners(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('spend: %s' % (end - start))
    return inners


@show_spend_time
def add(*args, **kwargs):
    num = 0
    for i in args:
        num += i
    print(num)


add(1, 2, 3, 4, 4)




# 装饰器参数
def logger(flag = ''):
    def show_spend_time(func):
        def inners(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print('spend: %s' % (end - start))
            if flag == 'true':
                print('日志记录了')
        return inners
    return show_spend_time

@logger('true')
def add(*args, **kwargs):
    num = 0
    for i in args:
        num += i
    print(num)


@logger()
def add1(*args, **kwargs):
    num = 0
    for i in args:
        num += i
    print(num)
    print('没有记录')

add(1, 2, 3, 4, 4)
add1(1, 2)


