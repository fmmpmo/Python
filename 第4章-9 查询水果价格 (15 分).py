dic = dict()
dic[1] = 3.00
dic[2] = 2.50
dic[3] = 4.10
dic[4] = 10.20
lst = list(map(int, input().split()))
print('[1] apple')
print('[2] pear')
print('[3] orange')
print('[4] grape')
print('[0] exit')
for i in range(0, len(lst)):
    if i == 5 or lst[i] == 0:
        break
    elif lst[i] < 0 or lst[i] > 4:
        print('price = 0.00')
    else:
        print('price = {:.2f}'.format(dic[lst[i]]))