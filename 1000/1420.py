a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            a[j],a[i]=a[i],a[j]
for i in range(n):
    print(a[i])

