# author: chenjie
# date: 2018/10/30

# 列表生成式
a = [x * 2 for x in range(10)]
print(a)

def func(n):
    return n ** 3

b = [func(x) for x in range(10)]

print(b)

print(type(b))    # <class 'list'>

# 生成器
# 生成器的2种创建方式：
# 1 yield
# 2 (x * 2 for x in range(5))


s = (x * 2 for x in range(5))

print(s)    # <generator object <genexpr> at 0x1008051a8>

print(next(s))    # 0   等价于  s.__next__   在 py2 中：s.next()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
# print(next(s))  # StopIteration

print(''.center(50, '*'))

y = (x * 2 for x in range(5))
# 生成器就是一个可迭代对象（Iterable）
for i in y:
    print(i)


print(''.center(50, '*'))

def foo():
    print('ok')
    yield 10
    print('ok2')
    yield 1


d = foo()

print(d)    # <generator object foo at 0x1026ef2b0>
for i in d:
    print(i)


# 什么是可迭代对象 (对象拥有 __iter__() 方法的成为可迭代对象)

print(''.center(50, '*'))

# 0 1 1 2 3 4 5 13 21

# 斐波那契 (生成器例子 )
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield a
        a, b = b, a + b
        n = n + 1



g = fib(10)

print(g)

for i in g:
    print(i)


