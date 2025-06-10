a = []
n = int(input())
for i in range(n):
    name,grade = input().split()
    a.append([name, int(grade)])
min = a[0][1]
for i in range(n-1):
    for j in range(i+1,n):
        if a[i][1] > a[j][1]:
            a[j],a[i]=a[i],a[j]
print(a[n-3][0])
        

