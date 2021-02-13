n = int(input())
res = ''
maxn = 0
for i in range(0, n):
    s = input()
    if len(s) > maxn:
        maxn = len(s)
        res = s
print('The longest is:', res)