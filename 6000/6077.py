a = input()
a = int(a)
sum = 0
for i in range (a+1):
    if i%2==0:
        sum+=i
    i+=1
print(sum)
