a = int(input())
b = input().split()
b = list(map(int, b))
for i in range(a-1):
    flag = 0
    for j in range(a-1-i):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
            flag = 1
    if flag == 0:
            print(i)
            break
if flag == 1:
     print(a-1)