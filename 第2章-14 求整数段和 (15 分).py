a, b = map(int, input().split())
cnt = 0
sum = 0
for i in range(a, b + 1):
    cnt += 1
    sum += i
    print('{:>5}'.format(i), end='')
    if (cnt % 5 == 0 or i == b):
        print()
print('Sum = {}'.format(sum))