s = input()
s = s[-1::-1]
i = 0
while i < len(s) and s[i] == '0':
    i += 1
if i < len(s):
    print(s[i:])
else:
    print(0)