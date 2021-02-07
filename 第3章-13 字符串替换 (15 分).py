str = input()
res = ""
for i in str:
    if i >= 'A' and i <= 'Z':
        res += chr(ord('A') - ord(i) + ord('Z'))
    else:
        res += i
print(res)