import os

# if os.path.exists(f.name):
#     os.remove(f.name)
#     print(f'{f.name} deleted')
# else:
#     print(f"{f.name} does not exist")
f = open('/Users/zou/Documents/GitHub/web/test3.txt','w')

f.write('第一行\n第二行\n第三行\n')
f.close()

# f = open('/Users/zou/Documents/GitHub/web/test3.txt','r')
# s = f.readline().strip()
# print(s)
# s = f.readline().strip()
# print(s)
# f.close()

f = open('/Users/zou/Documents/GitHub/web/test3.txt','r')
s = f.readlines()
print(s)
