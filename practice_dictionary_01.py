# dictionary与list的区别
#   list 是有序的对象集合
#   dictionary 是无序对象的集合
# 字典使用{}定义
# 字典使用 键值对 存储数据，键值对 之间使用 , 分隔
#    键（key）是索引（index）
#    值（ value）是数据
#    键 和 值 之间使用 ： 分隔
#    键必须是唯一的
#    值 可以取任何数据类型，但键 只能使用 字符串、数字或 元组
xiaoming = {
    "name":"小明",
    "age":18,
    "gender":True,
    "height":175
}
print(xiaoming)
#  dictionary 取值
xiaoming["name"]
print(xiaoming["name"])

#  dictionary 修改
xiaoming["age"] = 19
#  dictionary 新增
#  如果key 不存在 ，即新增，存在即修改
xiaoming["hobby"] = "footboll"

# dictionary 删除
xiaoming.pop("name")

print(xiaoming)  #顺序随机

# dictionary 其它常用操作
# 统计键值对的数量
print(len(xiaoming))
#合并 dictionary
temp_dict = {"height":189,
             "age":30}
# 如果合并时，有重复的key，则更新。
xiaoming.update(temp_dict)
#清空 clear


# 遍历 字典
for i in xiaoming:
    print("%s - %s" % (i,xiaoming[i]))
