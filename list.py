# -*- coding: utf-8 -*-

# 定义列表
list = ['a', 'b', 'c']

# 通过下标访问列表中的元素，下标从0开始计数
print(list[0])  # a
print(list[1])  # b
print(list[2])  # c

# 还可以倒着取从-1开始计数
print(list[-1]) # c

# 切片：取多个元素
names = ["Bob", "Tenglan", "Eric", "Rain", "Tom", "Amy"]

# 取下标1至下标4之间的数字，包括1，不包括4
print(names[1:4])   # ["Tenglan", "Eric", "Rain"]

# 取下标1至-1的值，不包括-1
print(names[1:-1])  # ["Tenglan", "Eric", "Rain", "Tom"]

# 取下标0至3的值，不包括3
print(names[0:3])   # ['Bob', 'Tenglan', 'Eric']
print(names[:3])

# 如果想取最后一个，必须不能写-1，只能这么写
print(names[1:])    # ['Tenglan', 'Eric', 'Rain', 'Tom', 'Amy']

# 后面的2是代表，每隔一个元素，就取一个
print(names[0::2])  # ['Bob', 'Eric', 'Tom']
print(names[::2])

# 追加
names.append('我是新来的')
print(names)

# 插入
names.insert(2, '强行从Eric前面插入')
print(names)

names.insert(5, '从Eric后面插入试试新姿势')
print(names)

# 修改
names[2] = '该换人了'
print(names)

# 删除
del names[2]
print(names)

# 删除指定元素
names.remove('Eric')
print(names)

# 删除列表最后一个值，返回被删掉的值
ret = names.pop()
print(ret)
print(names)

# 扩展
names.extend(list)
print(names)

# 拷贝
# 需要详细研究

# 统计
print(names.count('Bob'))

# 排序，反转
names.sort()    # 排序
print(names)

names.reverse() # 反转
print(names)

# 获取下标
print(names.index('Amy'))   # 只返回找到的第一个下标

# 元祖
# 元组其实跟列表差不多，也是存一组数，只不过它一旦创建，便不能再修改，所以又叫只读列表

# 语法
name = ('jack', 'rose', 'bob')

# 方法
# count 和 index

