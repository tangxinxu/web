name_list = ['sam','li','tang']
name_list_01 = ['rrrr','tttt','sdada']
num_list_01 = [2,4,6,8,10,1]

# 1 取值和索引值

print(name_list[0])   #取值
print(name_list.index('li'))   #取索引

# 2 修改list

name_list[1] = 'lisi'
# IndexError: list assignment index out of range
# 修改超出索引范围时，程序会报错
# name_list[4] = 'liu'

# 3 增加

# addend 在列表末尾追加一个？数据
name_list.append('wang')
# insert 在列表中指定的索引位置插入数据
name_list.insert(1,'zhang')
# extend 把其它列表中的所有数据，追加当前列表末尾
name_list.extend(name_list_01)

# 4 删除
# clear
# 清空列表
# name_list.clear()

# pop
# 默认删除最后一个对象数据。可以指定索引
name_list.pop(5)

# remove
# 指定删除元素
# 从列表中删除第一次出现的数据，如果不存在即会报错。
name_list.remove('zhang')

# del
# 和remove有什么区别
# del 本质上将一个变量从内存中删除
# 日常操作list时，建议使用list提供的方法

# 5 统计
# len（length 长度）函数可以统计列表中元素的总数
list_len = len(name_list)

print('list中有%d个元素'%list_len)

# conunt 方法可以统计列表中的某一个数据出现的次数
list_count = name_list.count('sam')
print('list中sam出现的次数是%d次'% list_count)

排序
升序 sort
name_list.sort()
num_list_01.sort()

# 降序 sort(reverse = True)
name_list.sort(reverse=True)
num_list_01.sort(reverse=True)

# 逆序 （反转）
# 不进行逻辑排序，仅是反转顺序
num_list_01.reverse()

print(name_list)
print(num_list_01)
