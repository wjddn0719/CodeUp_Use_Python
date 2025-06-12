a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
for i in range(a-1):
    for j in range(i+1, a):
        if b[i]>b[j]:
            b[i],b[j]=b[j],b[i]
for i in range(a):
    print(b[i])
