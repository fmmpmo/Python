a = b = 1
n = int(input())
while True:
    t = a + b
    a = b
    b = t
    if t > n:
        print(t)
        break