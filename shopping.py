# -*- coding: utf-8 -*-

product_list = [
    ['mac', 12000],
    ['kindle', 4000],
    ['book', 17],
    ['car', 20]
]

car_list = []

saving = input('请输入您的金额：')

if saving.isdigit():
    saving = int(saving)

for i, v in enumerate(product_list, 1):
    print(i, '>>>', v)

while True:
    choice = input('请输入您要购买的商品序号【退出为q】：')

    if choice.isdigit():
        choice = int(choice)
        if choice > 0 and choice <= len(product_list):
            p_item = product_list[choice - 1]
            if saving > p_item[1]:
                saving -= p_item[1]
                car_list.append(p_item)
                print(car_list)
            else:
                print('您的余额不足, 还剩%s元' % saving)
        else:
            print('请输入正确的商品序号')

    elif choice == 'q':
        print('您购买的商品如下'.center(50, '-'))
        for i in car_list:
            print(i)
        print('您的余额为%s' % saving)
        break

    else:
        print('输入错误')
