a, m, d, n = input().split()
a = int(a)
m= int(m)
d=int(d)
n=int(n)
sum=int(a)
for i in range(1,n):
    sum = sum*m+d
print(sum)
