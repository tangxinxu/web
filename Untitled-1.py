def x(h):
    if h>32:
        print("大于32")
    else:
        print("小于32")
print("ssss")

x(21)
#age = int(input('请输入你的年龄'))
#if age < 18:
    #print("未成年🔞你好")
#else:
    #print('欢迎来到成人世界')

print("hu" * 3)
s = "python"
for char in s:
    print(s.index(char),char)
for i in range(len(s)):
    print(s[i])


for i in range(12):
    print(i)

a_list = [1,2,3]
a_list.append(5)
print(a_list)

import random
y = 1
a = random.randint(0,100)
b = int(input('请输入0-100中一个数字\n然后查看是否与电脑一样：'))
while a != b:
    if a > b:
        print('你第%d输入的数字小于随机数字')
        b = int(input('请再次输入'))
    else:
        print('你输入的大于电脑随机数')
        b = int(input("请再次输入"))

else:
    print("恭喜你猜对了")


