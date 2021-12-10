# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

# 1. 数据存到文件里的格式
#    姓名，年龄，手机，身份证，学科
# 2. 要确保手机、身份证，在文件里同样的数据只有一条。 可以文件里的手机和身份证号这2列，加载到内存里，以
#   以列表形式存放。用户一输入相关列，就到列表里检查有没有重复的
# 3. 选学科 时，给用户列出来选项，供选择
db_file = "student_data.db"

def validate_phone(num):
    if not num.isdigit():
        exit("手机号必须是数字")
    if len(num) != 11:
        exit("手机号必须达到11位")

    return True

def register_api():
    stu_data = {} # 为了后边存学员数据
    print("欢迎来到路飞学城".center(50,"-"))
    print("请完成学籍注册")
    name = input("姓名:").strip()
    age = input("年龄:").strip()
    phone = input("手机号:").strip()
    if phone in phone_list:
        exit("该手机已注册.")
    validate_phone(phone)

    id_num = input("身份证号:").strip()
    if id_num in id_num_list:
        exit("该身份证号已注册.")

    course_list = ["Python开发","Linux云计算","网络安全","数据分析&机器学习","前端开发"]
    for index,course in enumerate(course_list):
        print(f"{index}. {course}")

    selected_course = input("选择想学的课:")
    if selected_course.isdigit():
        selected_course = int(selected_course)
        if selected_course >= 0 and selected_course < len(course_list): # 合法选项
            picked_course = course_list[selected_course] # 选 中的课程
        else:
            exit("不合法的选项...")
    else:
        exit("非法输入..")

    stu_data["name"] = name
    stu_data["age"] = age
    stu_data["phone"] = phone
    stu_data["id_num"] = id_num
    stu_data["course"] = picked_course

    return stu_data


def commit_to_db(filename,stu_data):
    """
    把学员数据，存到文件 里
    :param filename: 学员数据库文件
    :param stu_data: 单个学员数据的dict
    :return:
    """
    f = open(filename,"a")
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id_num']},{stu_data['course']}\n"
    f.write(row)
    f.close()

def load_validated_data(filename):
    f = open(filename)
    phone_list = []
    id_num_list = []
    for line in f:
        line = line.split(",")
        phone = line[2]
        id_num = line[3]
        phone_list.append(phone)
        id_num_list.append(id_num)

    return phone_list,id_num_list

phone_list,id_num_list = load_validated_data(db_file)

student_data = register_api()
print(student_data)
commit_to_db(db_file,student_data)
