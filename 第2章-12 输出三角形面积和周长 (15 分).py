a, b, c = map(int, input().split())
if (a + b > c and a + c > b and b + c > a):
    s = (a+b+c)/2
    print('area = {:.2f}; perimeter = {:.2f}'.format(
        ((s * (s - a) * (s - b) * (s - c)) ** 0.5), a + b + c))
else:
    print('These sides do not correspond to a valid triangle')