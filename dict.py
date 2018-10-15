# -*- coding: utf-8 -*-

# 字典操作

# 语法
area = {
    '湖北': '武汉',
    '湖南': '长沙',
    '杭州': '西湖'
}

area1 = {
    '湖北': '武汉',
    '湖南': '长沙',
    '杭州': '西湖'
}

# 特性
# 字典是无序的
# key 必须是唯一的，天生去重

# 增加
area['四川'] = '成都'
print(area)

# 删除
area.pop('四川') # 返回删除的值
print(area)

del area['杭州'] # 直接删除对应的键和值
print(area)

area.popitem()  # 随机删除
print(area)

# 修改
area['湖北'] = '天门'
print(area)

# 查找
print('湖北' in area) # 返回布尔值

print(area.get('湖北')) # 返回键的值

print(area['湖北'])   # 返回键的值

# print(area['湖南']) # 如果一个key不存在，就报错，get不会，不存在只返回None

# values
print(area1.values())

# keys
print(area1.keys())

# items
print(area1.items())

# setdefault
print(area1.setdefault('湖北', '孝感')) # 存在就返回原来的值，不存在就添加新的键值对

# update
b = {1: 2, 3: 4}
ret = area1.update(b)
print(ret)

# 多级字典嵌套及操作
av_catalog = {
    "欧美": {
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩": {
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆": {
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

print(av_catalog["大陆"]["1024"])

# 循环dict

for i in area1:
    print(i, area1[i])

# 会先把dict转成list，数据大时不要用，消耗性能
for i, v in area1.items():
    print(i, v)





