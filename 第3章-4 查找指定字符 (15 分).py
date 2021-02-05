ch = input()
s = input()
if s.rfind(ch) != -1:
    print('index = {}'.format(s.rfind(ch)))
else:
    print('Not Found')