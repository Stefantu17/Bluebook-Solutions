import math

n = int(input())
lst = []
lst2 = []

for i in range(n):
    num = int(input())
    lst.append(num)

for i in lst:
    if i <= 30:
        lst2.append(38)
    elif i <= 50:
        lst2.append(55)
    elif i <= 100:
        lst2.append(73)
    elif i > 100:
        var = ((i - 100) / 50)
        var = math.ceil(var)
        lst2.append(73 + (24 * var))

for i in lst2:
    print(i)