#名片字典
card_list = []


def login_ui():
    print("*"*50)
    print("欢迎使用名片管理系统V0.1")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*"*50)
def add_card_info():  #名片输入
    name_str = input("请输入姓名：")
    phone_str = input("请输入手机号码：")
    qq_str = input("请输入QQ号码：")
    email_str = input("请输入电子邮箱：")
    card_dictionary = {"name":name_str,
                       "phone":phone_str,
                       "qq":qq_str,
                       "email":email_str}
    card_list.append(card_dictionary)

def new_card():
    '''新增名片'''
    print("-"*50)
    print("新增名片")
    print("-" * 50)
    add_card_info() ##

def show_all():
    '''显示所有名片'''
    print("-" * 50)
    print("显示所有名片")
    print("-" * 50)
    if len(card_list) == 0:  #判断表格是否为空
        print("当前无名片记录，请先新增名片")
        return
    # 打印表头
    for table_name in ["姓名", "手机号码", "QQ号码", "电子邮箱"]:
        print(table_name, end="\t\t")
    print("")
    print("=" * 50)
    # 打印表格
    for i in card_list:  #遍历列表
        print("%s\t\t%s\t\t%s\t\t%s\t\t"%(i["name"],i["phone"],i['qq'],i['email']))
def search_card():
    '''搜索名片'''
    print("-" * 50)
    print("搜索名片")
    print("-" * 50)
    search_name = input("请输入姓名：")
    if len(card_list) == 0:
        print("名片为空，请新增名片")
    else:
        for n in card_list:
            if n["name"] == search_name:
                print("找到了")
                print("%s\t\t%s\t\t%s\t\t%s\t\t"%(n["name"],n["phone"],n['qq'],n['email']))
                break
            else:
                print("找不到你要搜索的名片")




