num=int(input("Enter the number: "))

bit=0
while(num>0):
    if(num%2==1):
        bit=bit+1
    num=num//2

print("Set bit the number:",bit)
