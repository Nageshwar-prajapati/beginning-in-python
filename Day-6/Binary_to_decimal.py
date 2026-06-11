num=int(input("Enter the binary number: "))

i=0
sum=0
while(num>0):
    rem=num%10
    num=num//10
    sum=sum+rem*(2**i)
    i=i+1

print("Decimal number:",sum)
