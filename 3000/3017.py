a = int(input())
b = []
for i in range(a):
    b.append(input().split())
i=1
for row in b:
    row.append(i)
    i+=1
for row in b:
    for i in range(2):
        row[i]= int(row[i])
for j in range(a-1):
    for i in range(a-1):
        if (b[i][0] < b[i+1][0]) or \
            (b[i][0] == b[i+1][0] and b[i][1] < b[i+1][1]) or \
            (b[i][0] == b[i+1][0] and b[i][1] == b[i+1][1] and b[i][2] > b[i+1][2]):
                b[i], b[i+1] = b[i+1], b[i]

for i in range(a):
    print(b[i][-1],b[i][0],b[i][1])

    