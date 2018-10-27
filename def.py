# -*- coding: utf-8 -*-

# 函数的作用
# 1.减少重复代码
# 2.方便修改,更易扩展
# 3.保持代码的一致性

# define 定义

def sayHi():    # 函数名
    print('你好，世界')

sayHi() # 调用函数


# 可以带参数

# 下面这段代码
a, b = 5, 8
c = a * b
print(c)

# 改成用函数写
def calc(x, y):
    res = x * y
    return res # 返回函数执行结果

data = calc(10, 10)
print(data)


# 函数参数与局部变量
'''
【形参】 变量只有在被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此，形参只在函数内部有效。函数调用结束返回主调用函数后则不能再使用该形参变量
【实参】 可以是常量、变量、表达式、函数等，无论实参是何种类型的量，在进行函数调用时，它们都必须有确定的值，以便把这些值传送给形参。因此应预先用赋值，输入等办法使参数获得确定值
'''

# 默认参数
def stu_register(name, age, course, country="CN"):
    pass

# 这样，这个参数在调用时不指定，那默认就是CN，指定了的话，就用你指定的值。

# 关键参数
# 正常情况下，给函数传参数要按顺序，不想按顺序就可以用关键参数，只需指定参数名即可，但记住一个要求就是，关键参数必须放在位置参数之后。
stu_register(age=22,name='alex',course="python")

# 非固定参数
# 若你的函数在定义时不确定用户想传入多少个参数，就可以使用非固定参数

def stu_register(name, age, *args): # *args 会把多传入的参数变成一个元组形式
    print(name, age, args)

stu_register("Alex",22)
# 输出
# Alex 22 () #后面这个()就是args,只是因为没传值,所以为空

stu_register("Jack",32,"CN","Python")
# 输出
# Jack 32 ('CN', 'Python')

# 还可以有一个**kwargs
def stu_register(name, age, *args, **kwargs): # *kwargs 会把多传入的参数变成一个dict形式
    print(name,age,args,kwargs)

stu_register("Alex",22)
# 输出
# Alex 22 () {}#后面这个{}就是kwargs,只是因为没传值,所以为空

stu_register("Jack",32,"CN","Python",sex="Male",province="ShanDong")
# 输出
# Jack 32 ('CN', 'Python') {'province': 'ShanDong', 'sex': 'Male'}


# 局部变量
name = "Alex Li"

def change_name(name):
    print("before change:",name)
    name = "金角大王,一个有Tesla的男人"
    print("after change", name)


change_name(name)

print("在外面看看name改了么?", name)

# 输出
# before change: Alex Li
# after change 金角大王,一个有Tesla的男人
# 在外面看看name改了么? Alex Li

# 全局与局部变量
# 在子程序中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
# 全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序。
# 当全局变量与局部变量同名时：
# 在定义局部变量的子程序内，局部变量起作用；在其它地方全局变量起作用。


# 返回值
# 要想获取函数的执行结果，就可以用return语句把结果返回
# return 的作用
# 1.函数在执行过程中只要遇到return语句，就会停止执行并返回结果，so 也可以理解为 return 语句代表着函数的结束
# 2.要想获取函数的执行结果，就可以用return语句把结果返回

# 注意点
# 函数里如果没有return，会默认返回一个None
# 如果return多个对象，那么python会帮我们多个对象封装成一个元祖


