num=int(input("Enter the number: "))
n=num
sum=0
while(n>0):
    fac=1
    rem=n%10
    n=n//10
    for i in range(1,rem+1):
        fac=fac*i
    sum=sum+fac

if(num==sum):
    print("Strong number.")

else:
    print("Not strong number.")