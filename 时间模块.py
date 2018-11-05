# author: chenjie
# date: 2018/11/4

import time

print(help(time))

# print(time.time())  # 1541421435.381387 时间戳

# time.sleep(3)

# print(time.clock())     # 计算cpu执行时间

# print(time.gmtime())    # 结构化时间：time.struct_time(tm_year=2018, tm_mon=11, tm_mday=5, tm_hour=12, tm_min=50, tm_sec=34, tm_wday=0, tm_yday=309, tm_isdst=0)


print(time.localtime())   # 本地时间(结构化时间)：time.struct_time(tm_year=2018, tm_mon=11, tm_mday=5, tm_hour=20, tm_min=55, tm_sec=14, tm_wday=0, tm_yday=309, tm_isdst=0)

struct_time = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time))   # 2018-11-05 21:03:10 字符串时间

print(time.strptime('2018-11-05 21:06:49', '%Y-%m-%d %H:%M:%S'))    # time.struct_time(tm_year=2018, tm_mon=11, tm_mday=5, tm_hour=21, tm_min=6, tm_sec=49, tm_wday=0, tm_yday=309, tm_isdst=-1)

print(time.ctime(3600))

print(time.mktime(struct_time))     # 1541423938.0

import datetime

print(datetime.datetime.now())  # 2018-11-05 21:22:19.886468

