# author: chenjie
# date: 2018/10/21

# 深浅拷贝

# 浅拷 = 只拷贝第一层

# 深拷 = 克隆一份


# copy()

husband = ['xiaohu', 123, [15000, 7000]]
wife = husband.copy()

wife[0] = 'xiaobai'
wife[1] = 234

husband[2][1] -= 5000

print(wife)

import copy
# 浅拷贝
# xiaosan = copy.copy()

# 深拷贝
xiaosan = copy.deepcopy(husband)
