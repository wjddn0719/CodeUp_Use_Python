r, g, b= input().split()
r = int(r)
g = int(g)
b = int(b)
for i in range (r):
    for j in range (g):
        for k in range(b):
            print(i,j,k)
    i+=1
    j+=1
    k+=1
print(r*b*g)
