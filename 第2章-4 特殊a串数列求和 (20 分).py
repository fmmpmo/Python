a, n = input().split()
print('s = {}'.format(sum([int(a*i) for i in range(1, int(n)+1)])))