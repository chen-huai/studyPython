# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

def stu_register(name, age, course='PY', country='CN'):
    print("----注册学生信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)
    if age > 22:
        return False
    else:
        return True,age,name,course

    print("hahah我还在")



registriation_status = stu_register("王山炮", 21, course="PY全栈开发", country='JP')
print(registriation_status)
if registriation_status:
    print("注册成功")
else:
    print("too old to be a student.")

# 返回执行结果
# 程序执行，一遇到return ,就代表着函数的结束