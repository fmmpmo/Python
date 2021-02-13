s = input()
res = ''
for i in s:
    if i >= 'A' and i <= 'Z' and i not in res:
        res += i
if len(res) == 0:
    print('Not Found')
else:
    print(res)