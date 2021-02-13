def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5+1)):
        if n % i == 0:
            return False
    return True

m, n = input().split()
cnt = sum = 0
for i in range(int(m), int(n) + 1):
    if isprime(i):
        cnt += 1
        sum += i
print(cnt, sum)