str = input()
res = ""
for i in str:
    if (i >= '0' and i <= '9'):
        res += i
i = 0
while i < len(res) and res[i] == '0':
    i += 1
if i < len(res):
    print(res[i:])
else:
    print(0)