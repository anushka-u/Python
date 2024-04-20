n = int(input())

while(n<=10 and n!=0):
    print(n)

    if(n==1):
        break;
    n -= 1
else:
    print(" N is greater than 10")