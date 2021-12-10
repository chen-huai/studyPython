# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

db_file = "student_data.db"

def load_validated_data(filename):
    f = open(filename)
    registered_phones = []
    registered_id_nums = []
    for line in f:
        line = line.split(",")
        registered_id_nums.append(line[3])
        registered_phones.append(line[2])

    return registered_phones,registered_id_nums

def commit_to_db(filename,stu_data):
    """
    写入文件的格式
    姓名,年龄,手机，身份证，所选课程
    :param filename:
    :param stu_data:
    :return:
    """
    f = open(filename,"a")
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id_num']},{stu_data['course']}\n"
    f.write(row)
    f.close()


def register_interface():
    stu_data = {} # 存学员输入的信息
    name = input("姓名:").strip()
    age = input("年龄:").strip()
    phone = input("手机:").strip()
    if phone in phones:
        exit("手机号已存在.")
    id_num = input("身份证:").strip()
    if id_num in id_nums:
        exit("身份证已存在.")
    course_list = ["Python开发","Linux运维","网络安全","数据分析&机器学习","前端开发"]
    for index,course in enumerate(course_list):
        print(f"{index}. {course}")
    selected_course = input("选择要学的课程:").strip()
    if selected_course.isdigit():
        selected_course = int(selected_course)
        if selected_course >=0 and selected_course < len(course_list):
            stu_data["course"] = course_list[selected_course]
        else:
            print("invalid choice.")
    else:
        print("invalid input.")

    stu_data["name"] = name
    stu_data["age"] = int(age)
    stu_data["phone"] = int(phone)
    stu_data["id_num"] = id_num

    print(stu_data)
    return stu_data


phones,id_nums = load_validated_data(db_file) # 把要验证的2列数据提出来

data = register_interface()
commit_to_db(db_file,data)
