def calc(i):                               # 10
    print(i)                               # 10
    if int(i / 2) > 0:                     #  True
        calc(int(i / 2))                   #    5 2 1 ----
    else:
        print('----')
    print(i)


calc(10)



data_list = list(range(0, 101))

# 二分
def b_search(n, low, high, d):
    mid = int((low + high) / 2)
    if low == high:
        print('not found')
        return
    if d[mid] > n:
        print('go lefr：', low, high, d[mid])
        b_search(n, low, mid, d)
    elif d[mid] < n:
        print('go right:', low, high, d[mid])
        b_search(n, mid + 1, high, d)
    else:
        print('find it', d[mid])

b_search(10, 0, len(data_list), data_list)


import os

import time


ret = time.strftime('%Y-%m-%d %X')
print(ret)

print(os.getcwd())

# 日志模块logging模块
# 时间模块time
# 随机模块random
# 系统模块 os


