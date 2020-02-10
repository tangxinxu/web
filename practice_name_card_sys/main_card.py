import tool_card



while True:  # 无限循环
    # 调用显示功能菜单
    tool_card.login_ui()

    user_choice = input("请选择操作功能：")
    # 选择功能
    if user_choice in ["1","2","3"]:
        # 新增名片
        if user_choice == "1":
            tool_card.new_card()
        # 显示全部名片
        elif user_choice == "2":
            tool_card.show_all()
            print("")
        # 搜索名片
        elif user_choice == "3":
            tool_card.search_card()
        print("你选择的是功能是%s" % user_choice)
    # 退出
    elif user_choice == "0":
        print("欢迎再次使用")
        break
    # 选择错误
    else:
        print("你输入的不正确，请重新选择")
