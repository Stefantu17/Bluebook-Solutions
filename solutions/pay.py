n = int(input())
lst = []
lst2 = []

for i in range(n):
    pay = float(input())
    hours = int(input())
    if hours > 40:
        hours += (hours - 40)
    tax = str(input()).lower()
    donation = str(input()).lower()
    lst.append([pay, hours, tax, donation])
    if (i+1) < n:
        e = input()

for person in lst:
    pay = (person[0] * person[1])
    if person[2] == "b":
        pay -= (pay * 0.10)
    elif person[2] == "c":
        pay -= (pay * 0.20)
    elif person[2] == "d":
        pay -= (pay * 0.29)
    elif person[2] == "e":
        pay -= (pay * 0.35)
    if person[3] == "y":
        pay -= 10
    pay = round(pay, 2)
    print(format(pay, '.2f'))