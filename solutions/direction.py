n = int(input())
lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

for i in lst:
    if i < 46:
        print("N")
    elif i < 135:
        print("E")
    elif i < 226:
        print("S")
    elif i < 315:
        print("W")
    else:
        print("N")
