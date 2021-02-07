str = input()
yuan = ['A', 'E', 'I', 'O', 'U']
cnt = 0
for i in str:
    if i >= 'A' and i <= 'Z' and i not in yuan:
        cnt += 1
print(cnt)