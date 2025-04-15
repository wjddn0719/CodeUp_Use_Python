a, m, d = input().split()
a = int(a)
m = int(m)
d = int(d)
sum = int(1)
while sum%a!=0 or sum%m!=0 or sum%d!=0:
    sum+=1
print(sum)
