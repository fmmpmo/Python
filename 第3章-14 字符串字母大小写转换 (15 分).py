str = input()
res = ""
for i in str:
    if i == '#':
        break
    elif i >= 'A' and i <= 'Z':
        res += chr(ord(i) + 32)
    elif i >= 'a' and i <= 'z':
        res += chr(ord(i) - 32)
    else:
        res += i
print(res)