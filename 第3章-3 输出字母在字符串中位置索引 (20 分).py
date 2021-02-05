s = input()
s1, s2 = input().split()
for i in range(0, len(s)):
    if s[len(s) - i - 1] == s1 or s[len(s) - i - 1] == s2:
        print('{} {}'.format(len(s)-i-1, s[len(s)-i-1]))