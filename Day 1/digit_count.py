num=int(input("Enter the number: "))

count=0
while(num!=0):
    count=count+1
    num=num//10

print("Digits in the number: ",count)