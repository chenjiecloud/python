# import time
# import datetime
# import os
# print(datetime.datetime.now())
# print(datetime.date.fromtimestamp(time.time()))
#
#
#
# # 三级菜单
# menu = {
#     '北京':{
#         '海淀':{
#             '五道口':{
#                 'soho':{},
#                 '网易':{},
#                 'google':{}
#             },
#             '中关村':{
#                 '爱奇艺':{},
#                 '汽车之家':{},
#                 'youku':{},
#             },
#             '上地':{
#                 '百度':{},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '男孩':{},
#                 '北航':{},
#             },
#             '天通苑':{},
#             '回龙观':{},
#         },
#         '朝阳':{},
#         '东城':{},
#     },
#     '上海':{
#         '闵行':{
#             "人民广场":{
#                 '炸鸡店':{}
#             }
#         },
#         '闸北':{
#             '火车战':{
#                 '携程':{}
#             }
#         },
#         '浦东':{},
#     },
#     '山东':{},
# }
# print(os.listdir('src'))
#
# src_list = os.listdir('src')
#
# # print(src_list[0])
#
# for i, k in enumerate(src_list, 1):
#     print(i, '>>>', k)
#
#
# city = {
#     '湖北': {
#         '武汉': {
#             '孝感': {
#
#             }
#         },
#         '随州': {
#
#         }
#     },
#     '长沙': {
#
#     }
# }
#
# print(city.items())
#
# for key in city:
#     print(key, city[key])
#
#
# def auth(context, *args):
#     print(context, *args)
#
# auth(1, '2', '2')
#
# ret = map(lambda x: x * 6, [1, 2, 3, 4, 5])
#
# for i in ret:
#     print(i)
#
#
# a = '你好'
# b = '世界'
# print('，'.join((a, b)))


# 集合
# 1.主要作用
# 2.关系测试，交集\差集\并集\反向（对称）差集

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a)
print(type(a))

a.symmetric_difference(b)
print(a.symmetric_difference(b))

print('你好'.center(50, '*'))



