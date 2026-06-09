num=int(input("Enter the number: "))

temp=num
rev=0
while(temp>0):
    rem=temp%10
    temp=temp//10
    rev=rev*10+rem

if(num==rev):
    print("It's palindrome")

else:
    print("Not palindrome")
    

