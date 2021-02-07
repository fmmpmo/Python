n = int(input())
num = map(int, input().split())
pos = res = 0
maxn = -99999
for i in num:
    if i > maxn:
        maxn = i
        res = pos
    pos += 1
print(maxn, res)