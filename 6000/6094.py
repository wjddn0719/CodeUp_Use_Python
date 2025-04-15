n = int(input())
a = input().split()
for i in range(n):
    a[i]=int(a[i])
sum = int(a[0])
for i in range(n):
    if a[i]<sum:
        sum=a[i]
print(sum)
