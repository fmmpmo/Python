weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
n = int(input())
cnt = 0
for i in range(0, n):
    sum = 0
    id = input()
    flag = 1
    for j in range(0, 17):
        if not id[j].isdigit():
            flag = 0
        else:
            sum += (int(id[j])) * weight[j]
    if flag == 1 and id[17] == check[sum % 11]:
        cnt += 1
    else:
        print(id)
if cnt == n:
    print('All passed')