a = []
n = int(input())
for i in range(n):
    a.append(input())
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]> a[j]:
             a[i], a[j]=a[j], a[i]
for i in range(5):
    print(a[i])

