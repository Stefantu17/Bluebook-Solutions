n = int(input())
lst = []

for i in range(n):
    num = float(input())
    lst.append(num)

lst = sorted(lst)

print(lst[0])