n = int(input())
if n == 3:
    for i in range(100, 1000):
        a = i // 100
        b = (i - a * 100) // 10
        c = i % 10
        if a * a * a + b * b * b + c * c * c == i:
            print(i)
elif n == 4:
    for i in range(1000, 10000):
        a = i // 1000
        b = (i - a * 1000) // 100
        c = (i - a * 1000 - b * 100) // 10
        d = i % 10
        if a * a * a * a + b * b * b * b + c * c * c * c + d * d * d * d == i:
            print(i)
elif n == 5:
    for i in range(10000, 100000):
        a = i // 10000
        b = (i - a * 10000) // 1000
        c = (i - a * 10000 - b * 1000) // 100
        d = (i - a * 10000 - b * 1000 - c * 100) // 10
        e = i % 10
        if a * a * a * a * a + b * b * b *b * b + c * c * c *c * c + d * d * d *d *d + e * e * e * e * e == i:
            print(i)