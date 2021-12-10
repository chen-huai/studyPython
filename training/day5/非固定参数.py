# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

def stu_register(name,age,*args,**kwargs): # *args 会把多传入的参数变成一个元组形式
    print(name,age,args,kwargs)
    print(kwargs["ad2dr"])

#stu_register("Alex",22)
stu_register("Alex",22,"M","Girl",13651054608,addr="山东省德州",hometown="城后李")

