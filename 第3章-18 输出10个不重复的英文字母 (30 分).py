s = input()
res = ''
for i in s:
    if i.isalpha() and i not in res and i.upper() not in res.upper():
        res += i
    if len(res) == 10:
        break
if len(res) < 10:
    print('not found')
else:
    print(res)