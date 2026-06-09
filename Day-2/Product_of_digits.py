num=int(input("Enter the number: "))

pro=1
while(num>0):
    rem=num%10
    num=num//10
    pro=pro*rem

print("Product of digits:",pro)