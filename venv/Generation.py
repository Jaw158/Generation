import random
a = 1
b = 1
c = 0
while b > 0:
    b = 0
    for i in range(a):
        x = random.randint(1, 6)
        if x == 1 or x == 2:
            y = 0
        elif x == 3 or x == 4:
            y = 1
        elif x == 5:
            y = 2
        else:
            y = 3
        b = b+y
    a = b
    c = c+1
    print(c, b)