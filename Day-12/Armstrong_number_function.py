def armstrong(n):
    num,num1,count=n,n,0
    sum=0
    while(num!=0):
        num=num//10
        count+=1

    while(num1!=0):
        rem=num1%10
        num1=num1//10
        sum=sum+(rem**count)

    return (sum==n)

num=int(input("Enter the number: "))

if(armstrong(num)):
    print("Armstrong number")

else:
    print("Not a armstrong number")