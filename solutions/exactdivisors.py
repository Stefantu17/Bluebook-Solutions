x = int(input(""))
y = 1

while y != (x+1):
    if (x/y) % 1 == 0:
        print(y)
    elif y == x:
        print(x)
        break
    y = y + 1