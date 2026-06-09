num=int(input("Enter the range: "))

print("Armstrong number between 1 and",num,":",end=" ")
for i in range(1,num+1):
    n=i
    m=i
    count=0
    sum=0
    while(n>0):
        count=count+1
        n=n//10

    while(m>0):
        rem=m%10
        m=m//10
        sum=sum+(rem**count)

    if(i==sum):
        print(i,end=" ")
