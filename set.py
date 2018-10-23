# author: chenjie
# date: 2018/10/22

# 集合 Sset

# 1.无序
# 2.不重复的

# 集合的创建
# 去重
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






