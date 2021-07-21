n = int(input())
a = 2
b = 1
sum = a / b
for i in range(2, n + 1):
    t = a
    a = a + b
    b = t
    sum += a / b
print('{:.2f}'.format(sum))