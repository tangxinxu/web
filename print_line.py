
# age = int(input('''Please tell me your age:
#  an int number , e.g: 22
# '''))
# if age < 18:
#     print('I can not sell you drinks...')
# else:
#     print('Have a nice drink!')

def line_1(X,num):
    """

    :param X: 分隔符
    :param num: 重复次数
    """
    print(X*num)



def line_2(y,n,rownum):
    """
打印多行分割线
    :param y: 分割线使用的分隔字符
    :param n: 每一行重复次数
    :param rownum: 行数设置
    """
    row = 0
    while row < rownum:
        line_1(y,n)

        row += 1

line_2('^',7,8)

