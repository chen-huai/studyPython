# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

d = {"name": "Alex", "age": 26, "hobbie": "大保健"}
l = ["Rebeeca", "Katrina", "Rachel"]

# set

def change_data(info, girls):
    info["hobbie"] = "学习"
    girls.append("XiaoYun")
    d = {}


change_data(d, l)
print(d, l)