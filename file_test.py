# 1、查
# 输入：www.oldboy.org
# 获取当前backend下的所有记录
#
# 2、新建
# 输入：
# arg = {
#     'bakend': 'www.oldboy.org',
#     'record':{
#         'server': '100.1.7.9',
#         'weight': 20,
#         'maxconn': 30
#     }
# }
#
# 3、删除
# 输入：
# arg = {
#     'bakend': 'www.oldboy.org',
#     'record':{
#         'server': '100.1.7.9',
#         'weight': 20,
#         'maxconn': 30
#     }
# }

entry = input('>>>：')

if entry == 'www.oldboy.org':
    f = open('./src/haproxy.cfg', 'r+', encoding='utf-8')
    data = f.read()
    print(data)
else:
    print('输入错误')
