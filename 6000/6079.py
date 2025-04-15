a = int(input())
sum = 0
i=0
while True:
    if(sum<a):
        i+=1
        sum+=i
    else:
        print(i)
        break
