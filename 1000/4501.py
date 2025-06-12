b = []
for i in range(7):
    b.append(int(input()))
for i in range(1, 7):
    key = b[i]
    j = i-1
    while j>=0 and key<b[j]:
        b[j+1] = b[j]
        j-=1
        b[j+1] = key
print(b[-1])
print(b[-2])