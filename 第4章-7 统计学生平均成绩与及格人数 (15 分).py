n = int(input())
if n > 0:
    sum = cnt = 0
    lst = list(map(int, input().split()))
    for i in lst:
        sum += i
        if i >= 60:
            cnt += 1
    print('average = {:.1f}'.format(sum / n))
    print('count =', cnt)
else:
    print('average = 0.0')  
    print('count = 0')