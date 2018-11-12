# author: chenjie
# date: 2018/10/30

# 列表生成式
a = [x * 2 for x in range(10)]
print(a)

def func(n):
    return n ** 3

b = [func(x) for x in range(10)]

print(b)

