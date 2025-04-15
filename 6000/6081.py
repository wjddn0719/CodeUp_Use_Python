a = input()
a = int(a, 16)
for i in range (1, 16):
    sum = a*i
    print('%X' %a, '*%X' %i, '=%X' %sum, sep='')
