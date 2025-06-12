a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
for i in range(1,a):
    key = b[i]
    j=i-1
    while j>=0 and key<b[j]:
        b[j+1]=b[j]
        j-=1
        b[j+1]=key
for i in range(a):
    print(b[i])


        