def perfectnum(n):
    sum=0
    for i in range(1,int(n/2)+1):
        if(n%i==0):
            sum+=i

    return (sum==n)

num=int(input("Enter the number: "))

if(perfectnum(num)):
    print("Perfect number")

else:
    print("Not a perfect number")