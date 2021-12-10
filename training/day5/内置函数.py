# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

# # abs 取绝对值
# print(abs(-10))
#
# # all 要求全部为True
# a = [0,2,3,4,5,6,7]
# print(all(a) )

# any ,  任意一个值为True
# a = [0,0]
# print(any(a) )
#
# print(chr(60))

# dict
# print(dict())
# print(dict(name="alex",age=22))

# dir 打印当前程序的所有变量名
# name = "alex"
# # age = 22
# # print(__file__)
# # print(dir())

# locals() 打印当前程序（当前作用域）的所有变量名 & 变量值
# name = "alex"
# age = 22
# print(locals())

# map
# l = list(range(10))
# print(l)
# def calc(x):  # 只能定义一个参数
#     return  x**2
#
# m = map(calc, l ) # 并没有执行 （迭代器）
# for i in m:  # 每循环一次，就把列表里的每一个元素扔给Calc函数执行，
#     print(i)

# max
# l = list(range(10))
# print(max(l))
# print(min(l))
# # sum
# print(sum(l))

# ord 打印ascii字符对的10进制数字
# print(ord("<"))
#
# for index,val in enumerate(['alex','jac']):
#     print(index,val)

# print(round(3.14159,2))  #输出 3.14
# a = str(list(range(10)))
# print(type(a))
#

# a = ["alex","jack","rain"]
# b = ["black girl", "racheal", "Cicy", "Cathrine"]
#
# for i in zip(a,b):
#     print(i)
# 输出
# ('alex', 'black girl')
# ('jack', 'racheal')
# ('rain', 'Cicy')


# # filter , 把列表里的每个元素交给第一个参数（函数）运行，若结果为真，则保留这个值 。
# l = list(range(10))
#
# def compare(x):
#     if x >5:
#         return x
#
# print(l)
# for i in filter(compare, l):
#     print(i)


