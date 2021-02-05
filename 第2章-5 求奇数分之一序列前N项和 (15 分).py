n = int(input())
print('sum = {:.6f}'.format(sum([1/i for i in range(1, 2*n) if i % 2 == 1])))