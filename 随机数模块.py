# author: chenjie
# date: 2018/11/5

import random

print(random.random())

print(random.randint(1, 8))    # 包括8

print(random.choice('hello'))

print(random.choice([1, 2, 3, [1, 2, 4]]))

print(random.sample([1, 2, 3, [1, 2, 4]], 2)) # 随机选取两个值

print(random.randrange(1, 3))


# 验证码

def v_code():
    code = ''
    for i in range(5):

        add_code = random.choice([random.randrange(10), chr(random.randrange(65, 91))])

        code += str(add_code)
    print(code)


v_code()


# print(chr(65))    A
# print(chr(91))    Z



