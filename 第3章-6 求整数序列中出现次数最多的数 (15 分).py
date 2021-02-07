str = input().split()
num = str[1:]
maxn = x = 0
for i in num:
    cnt = num.count(i)
    if cnt > maxn:
        maxn = cnt
        x = i
print(x, maxn)