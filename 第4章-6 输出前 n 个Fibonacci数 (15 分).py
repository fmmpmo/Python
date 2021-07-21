lst = list()
lst.append(1)
lst.append(1)

def fib():
    for i in range(2, 46):
        lst.append(lst[i-1]+lst[i-2])

n = int(input())
if n < 1:
    print('Invalid.')
else:
    cnt = 0
    fib()
    for i in range(1, n+1):
        cnt += 1
        print('{:>11}'.format(lst[i-1]), end='')
        if cnt % 5 == 0 or i == n:
            print()