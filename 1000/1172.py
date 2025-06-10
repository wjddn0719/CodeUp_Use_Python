a = list(map(int,input().split()))
for i in range(3):
    for j in range(i+1, 3):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
for i in range(3):
    print(a[i], end=" ")
