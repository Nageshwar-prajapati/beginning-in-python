num=int(input("Enter the number: "))

n=num
m=num
count=0
sum=0
while(n>0):
    count=count+1
    n=n//10

while(m>0):
    rem=m%10
    m=m//10
    sum=sum+(rem**count)

if(num==sum):
    print("Armstrong number.")

else:
    print("Not armstrong number.")