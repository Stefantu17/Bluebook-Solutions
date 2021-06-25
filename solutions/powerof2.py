n = int(input())
count = 0

while True:
    if 2 ** count >= n:
        print(count)
        break
    count += 1
