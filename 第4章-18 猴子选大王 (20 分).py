n = int(input())
s = [i for i in range(1, n+1)]
while len(s) >= 3:
    s = s[3:]+s[0:2]  # 去掉第三个，把前两个移到最后面
s *= 2
print(s[1])