a = int(input())
for i in range (1, a+1):
    if(bool(i%10!=3) and bool(i%10!=6) and bool(i%10!=9)):
        print(i, end=' ')
    elif(bool(i%10==3) or bool(i%10==6) or bool(i%10==9)):
        print("X", end=' ')
    i+=1
