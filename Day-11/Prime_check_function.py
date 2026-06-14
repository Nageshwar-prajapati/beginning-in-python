def checkprime(n):
    
    if (n<=1):
        return 0

    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return 0

    return 1


n=int(input("Enter the number: "))

if(checkprime(n)==1):
    print("Prime number.")

else:
    print("Not prime number.")