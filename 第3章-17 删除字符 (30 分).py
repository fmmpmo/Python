s = input().strip()
ch = input().strip()
for i in s:
    if i in ch or i.upper() in ch or i.lower() in ch:
        s = s.replace(i, '')
print('result:', s)