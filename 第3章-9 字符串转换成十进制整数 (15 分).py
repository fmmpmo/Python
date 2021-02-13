str = input()
check = '0123456789ABCDEFabcdef'
s = ''
for i in str:
    if i in check:
        s += i
if s == '':
    print('0')
elif str.find(s[0]) > str.find('-'):
    print(-1 * int(s, 16))
else:
    print(int(s, 16))