# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城


name = "Alex Li"
def change_name():
    #global name # 声明一个全局变量
    name = "金角大王,一个有Tesla的高级屌丝"
    print("after change", name)

change_name()
print("在外面看看name改了么?",name)

print(name)