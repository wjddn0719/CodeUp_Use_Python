n = input()
n = int(n)
for i in range(1, n+1):
    if i%3 != 0:
        print(i,end=" ")
    else:
        print("", end="")
