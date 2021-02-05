list = list(map(int, input().split()))
sum = 0
for i in list:
    sum += i
sum /= len(list)
for i in list:
    if i > sum:
        print(i, end=' ')