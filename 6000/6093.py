n = int(input())
num = input().split()
for i in range(n):
    num[i]=int(num[i])
for i in range(n-1, -1, -1):
    print(num[i], end=" ")
