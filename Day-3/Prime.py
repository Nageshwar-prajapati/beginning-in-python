num=int(input("Enter the number:"))

found=0
ran=(num//2)+1
for i in range(2,(num//2)+1):
    if(num%i==0):
        found=1
        break

if(found):
    print("Not prime.")

else:
    print("Prime")