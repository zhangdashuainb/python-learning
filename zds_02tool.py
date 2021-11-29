student_list = []  # 记录所有名字的字典


def show_menu():
    print("*" * 50)
    print("欢迎使用110信息管理系统V1.0")
    print(" 1.新建学生信息\n", "2.显示全部信息\n", "3.查询学生信息\n", "0.退出系统".ljust(1))
    print("*"*50)


def new_student():
    """新增学生信息"""
    print("新增学生信息")
    # 1. 提示用户输入学生信息详细信息
    name_str = input("请输入姓名：")
    number_str = input("请输入学号：")
    phone_str = input("请输入电话：")
    email_str = input("请输入邮箱：")
    # 2. 使用用户输入的信息建立一个名片字典
    card_1 = {"name": name_str,
              "number": number_str,
              "phone": phone_str,
              "email": email_str}
    # 3. 将名片字典添加到列表中
    student_list.append(card_1)
    print(student_list)
    # 4. 提示用户添加成功
    print("学生%s信息添加成功" % card_1["name"])


def show_all():
    """显示全部"""
    print("显示全部".center(36))
    # 判断是否存在学生记录，如果没有就返回
    if len(student_list) == 0:
        print("当前没有记录任何学生信息，请使用新增功能添加学生")
        return
    # 打印表头
    for biaotou in ["姓名", "学号", "电话", "邮箱"]:
        print(biaotou, end="\t\t\t\t")
    print("")
    # 打印分割线
    print("=" * 50)
    # 遍历列表依次输出信息
    for card_show in student_list:
        print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t" % (card_show["name"],
                                                            card_show["number"],
                                                            card_show["phone"],
                                                            card_show["email"]))


def search_card():
    """搜索学生信息"""
    print("-"*50)
    print("搜索学生信息")
    # 提示用户输入要搜索的名字
    find_name = input("请输入要搜索的姓名：")
    # 遍历名片列表，查询要搜索的姓名，如果没有找到，提示用户：
    for student_search in student_list:
        if student_search["name"] == find_name:
            print("找到了")
            # 打印表头
            for biaotou in ["姓名", "学号", "电话", "邮箱"]:
                print(biaotou, end="\t\t\t\t")
            print("")
            # 打印分割线
            print("=" * 50)
            # 遍历列表依次输出信息
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t" % (student_search["name"],
                                                                student_search["number"],
                                                                student_search["phone"],
                                                                student_search["email"]))
            del_card(student_search)
            break
    else:
        print("抱歉没有找到%s" % find_name)


def del_card(find_dict):
    """
    处理查找到的学生信息
    :param find_dict: 查找到的学生信息字典，形参
    :return:
    """
    print("")
    action_d = input("请输入操作指令1：修改/ 2：删除/  0：返回上级菜单：")
    # 修改寻找到的字典
    if action_d == "1":
        action_alter = input("请输入修改对象：1.姓名 / 2.学号 / 3.电话 / 4.邮箱 / 5.整体修改")
        if action_alter == "1":
            find_dict["name"] = input("请输入修改后姓名：")
            print("姓名修改成功")
        elif action_alter == "2":
            find_dict["number"] = input("请输入修改后学号：")
            print("学号修改成功")
        elif action_alter == "3":
            find_dict["phone"] = input("请输入修改后电话：")
            print("电话修改成功")
        elif action_alter == "4":
            find_dict["email"] = input("请输入修改后邮箱：")
            print("邮箱修改成功")
        elif action_alter == "5":
            find_dict["name"] = input_card_info(find_dict["name"], "请输入修改后姓名(空格不修改)：")
            find_dict["number"] = input_card_info(find_dict["number"], "请输入修改后学号(空格不修改)：")
            find_dict["phone"] = input_card_info(find_dict["phone"], "请输入修改后电话(空格不修改)：")
            find_dict["email"] = input_card_info(find_dict["email"], "请输入修改后邮箱(空格不修改)：")
        else:
            print("输入错误请输入正确的指令数字:1.修改姓名 / 2.修改学号 / 3.修改电话 / 4.修改邮箱 / 5.整体修改")
    # 删除寻找到的字典
    elif action_d == "2":
        student_list.remove(find_dict)
        print("删除学生信息成功")

    # 返回上一级菜单
    elif action_d == "0":
        print("返回上一级菜单")

    # 输入错误
    else:
        print("输入错误，请输入正确数字1：修改/ 2：删除/  0：返回上级菜单")


def input_card_info(dict_value, tip_message):

    """输入学生信息

    :param dict_value:字典原有的值
    :param tip_message:输入的提醒信息
    :return:如果用户输入了内容，就返回内容，否则返回字典中原本的值
    """
    # 提示用户输入内容
    result_str = input(tip_message)
    # 针对用户的输入进行判断，如果用户输入了内容，直接返回结果;
    if len(result_str) > 0:
        return result_str
    # 如果用户没有输入内容，返回字典本来的值
    else:
        return dict_value
