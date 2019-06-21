import random
r = random.randrange(1,1000)
if r > 300 :
    print('大于300')
else:
    print('小于300')



for i in range(1,100):
    if i == 2 :
        print(i)
    for n in range(2,i):
        if (i%n) == 0:
            break
    else:
        print(i)

