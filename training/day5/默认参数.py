# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

# def stu_register(name, age, country="CN", course ):

def stu_register(name, age, course,country="CN"):
    print("----注册学生信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)


stu_register("王山炮", 22, "python_devops")
stu_register("张叫春", 21,  "linux",country="JP")
stu_register("张叫阳", 21,  "linux","US")
stu_register("刘老根", 25, "linux")