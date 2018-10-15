# -*- coding: utf-8 -*-

# 字符串操作
# 特性：不可修改

# * 重复输出字符串
print('hello' * 10)

# [:] 通过索引获取字符串中字符
str = 'helloworld'
print(str[2:])

# in 判断 成员运算符 如果包含，返回True
print('ell' in str)

# % 格式化字符串
print('你好%s' % '世界')

# + 字符串拼接

# 消耗性能
a = '您好'
b = '世界'
print(a + b)

# 使用 join 函数
print('>>>>'.join([a, b]))

name = 'My name is Amy'

print(name.capitalize())    # 首字母大写
print(name.casefold())      # 大写全部变小写
print(name.center(50, '-')) # ------------------My name is Amy------------------
print(name.count('m'))      # 统计m出现的次数
print(name.encode())        # 将字符串编码成bytes格式
print(name.startswith('M')) # 判断字符串是否以 M 开头
print(name.endswith('M'))   # 判断字符串是否以 M 结尾
print('Bob\tAnda'.expandtabs(10)) # 输出 'Bob       Anda'，将\t转换成多长的空格
print(name.find('A'))       # 查找A, 找到返回其索引， 找不到返回-1

# format:
msg = 'my name is {}, and age is {}'
print(msg.format('Amy', 550))   # my name is Amy, and age is 550

msg = "my name is {1}, and age is {0}"
print(msg.format('Amy', 550))   # my name is 550, and age is Amy

msg = "my name is {name}, and age is {age}"
print(msg.format(name = 'Amy', age = 550))  # my name is Amy, and age is 550

# format_map:
print(msg.format_map({'name': 'ajax','age': 22}))   # my name is ajax, and age is 22


