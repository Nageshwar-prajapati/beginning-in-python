ran=int(input("Enter the range: "))

print("Prime number between 1 and",ran,":",end=' ')
for i in range(2,ran+1):
    found=0
    for j in range(2,(i//2)+1):
        if(i%j==0):
            found=1
            

    if(found==0):
        print(i,end=' ')