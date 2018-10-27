# 集合 Set

# 1.无序
# 2.不重复的

# 集合是一个无序的，不重复的数据组合，它的作用如下：

# 1.去重， 把一个列表变成集合，就自动去重了
# 2.关系测试，测试两组数据之前的交集，差集，并集，对称差集等关系

# 常用操作

s = set([1, 2, 3, 4, 5])    # 创建一个数值集合

t = set('hello')    # 创建一个唯一字符的集合

a = t | s   # t 和 s 的并集
print(a)

b = t & s   # t 和 s 的交集
print(b)

c = t - s   # 求差集（项在t中，但不在s中)
print(c)

d = t ^ s   # 对称差集（项在t或s中，但不会同时出现在二者中）
print(d)

# 基本操作
t.add('x')   # 添加一项

s.update([10, 11, 22])  # 在s中添加多项

# 使用remove() 可以删除一项：
t.remove('h')

# set的长度
len(s)

x = ''
# 测试 x 是否是 s 的成员
print(x in s)

# 测试 x 是否不是 s 的成员
print(x not in s)

s = set('cjl kl')

print(s) # {'j', 'c', 'l', ' ', 'k'}

# 由于集合本身是无序的，所以不能为集合创建索引或切片操作，只能循环遍历或使用迭代器来访问
# 使用in，not in 来判断是否存在于集合

# 更新集合
# add()

# 作为序列添加（去重）
# update


a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])


print(a.intersection(b)) # 交集
print(a.union(b)) # 并集
print(a.difference(b)) # 单向差集（a里面有，b里面没有）a - b
print(a.symmetric_difference(b)) # 对称差集 （反向交集）


# | 求并集
# - 求差集
# ^ 对称差集
# & 求交集

# 父集(超集)
print(a.issuperset(b))

# 子集
print(a.issubset(b))




