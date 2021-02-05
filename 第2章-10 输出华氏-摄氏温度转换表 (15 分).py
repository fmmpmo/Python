lower, upper = input().split()
lower = int(lower)
upper = int(upper)
if (lower > upper):
    print('Invalid.')
else:
    print('fahr celsius')
    for i in range(lower, upper + 1, 2):
        print('{}{:>6.1f}'.format(i, 5*(i-32)/9))