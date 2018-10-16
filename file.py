# -*- coding: utf-8 -*-

# 文件操作的流程

# 打开文件
# f = open('./src/lyrics.txt', encoding='utf-8')

# 读取文件，文件大时不要用
# data = f.read()
# print(data)

# 读取一行
# first_line = f.readline()
# print('first_line: ', first_line)

# 关闭文件
# f.close()

# open() 函数的具体用法
# 文件句柄 = open('文件路径', '模式', 编码方式)。

# 关于模式
# r ：只读模式（默认）
# w ：只写模式（不可读；不存在则创建新文件；存在则将其覆盖）
# a ：追加模式（可读；不存在则创建新文件；存在则只追加内容）

# r+ ：可读写文件（可读，可写，可追加）
# w+ ：可写读
# a+ ：追加模式（可读；不存在则创建新文件；存在则只追加内容）

# "b" ：表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
# rb ：以二进制格式打开一个文件用于只读。


# 只读模式 r
# f = open('./src/lyrics.txt', 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# 只写模式 w （存在会覆盖原来内容）
# f = open('./src/lyrics.txt', 'w', encoding='utf-8')
# f.write('作者：xxx')
# f.close()   # 写完后原来的内容全都不见了，只剩下'作者：xxx'.

# 追加模式 a
# f = open('./src/lyrics.txt', 'a', encoding='utf-8')
# f.write('作者：xxx')
# f.close()

# 以 r+ 模式打开
# f = open('./src/lyrics.txt', 'r+', encoding='utf-8')
# f.write('作者：xxxxxx')
# print(f.read())
# f.close()

# with 语句
# 为了避免打开文件后忘记关闭，可以通过管理上下文
# with open('./src/lyrics.txt') as f:

# py2.7以后，可以支持对多个文件的上下文进行管理
# with open('txt.txt') as obj1, open('txt2.txt') as obj2:

