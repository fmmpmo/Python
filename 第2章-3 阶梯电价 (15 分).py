x = float(input())
if x < 0:
    print("Invalid Value!")
elif x >= 0 and x <= 50:
    print('cost = {:.2f}'.format(x * 0.53))
else:
    print('cost = {:.2f}'.format(50*0.53+(x-50)*0.58))