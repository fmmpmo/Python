def fun(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

n = int(input())
sum = 1
for i in range(1, n + 1):
    sum += 1/fun(i)
print('{:.8f}'.format(sum))