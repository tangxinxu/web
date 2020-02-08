str_1 = 'hello world'
print(str_1[2])

for i in str_1:  #遍历str
    print(i)

# str长度
len(str_1)
print(len(str_1))
# str的计数
# 大小写分别统计
str_1.count('l')
print(str_1.count('l'))
# 子字符串的索引
print(str_1.index("h"))
# 索引对于的字符
print(str_1[6])
# 字符串的方法
# 类型判断
# 判断空白字符


print(str_1.isalnum())
# 查找替换
print(str_1.replace('l','hello'))
print(str_1)
# 大小写转换

# 文本对齐

# 取出空白字符


#拆分和连接

str_2 = "unexpected indent 就是 说 第二行 这里 存在 一个 “意外的” 缩进 。"
list_1 = str_2.split(' ')
print(list_1)
for word in list_1:
    print(word)
