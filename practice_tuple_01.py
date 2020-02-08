# tuple 与 list
# 元组 表示多个元素组成的序列
# 在python中有特定应用场景
# 元组中的元素是不能修改的
# 元组使用()
# 索引同样是从0开始的
info_tuple = ("zhang",18,175)

print(type(info_tuple))  #验证元组类型

# 索引
info_tuple[0]
print(info_tuple[0])

# 创建空元组
empty_tuple = ()  # 实际没人这么用
print(type(empty_tuple))

# 创建一个元素的元组
single_tuple = (5)
print(type(single_tuple))
single_tuple_01 = (5,)  #需在元素后加 ，
print(type(single_tuple_01))

# 元组的方法
# count
# empty_tuple.count()  # 空元组conunt会报错
# index
# empty_tuple.index()
# len
print(len(empty_tuple))


# 遍历tuple
for i in info_tuple:
    # 实际使用中tuple中的数据类型如果不一致，很少使用遍历
    print(i)

# 实际使用场景
# 1 函数的参数和返回值，一个函数可以接受任意多个参数，或者一次返回多个数据

# 2 格式字符串，格式化字符串后面的（），本质上就是一个元组
print("%s年龄是%d身高是%.0f" % info_tuple)

info_str = "%s年龄是%d身高是%.0f" % info_tuple

print(info_str)
# 3 让列表不可修改，保护数据安全
num_list = [1,2,3,4]
print(type(num_list))
num_tuple = tuple(num_list)
print(type(num_tuple))





