m, n = input().split()
m = int(m)
n = int(n)
sum = 0
for i in range(m, n + 1):
    sum += i * i + 1 / i
print('sum = {:.6f}'.format(sum))