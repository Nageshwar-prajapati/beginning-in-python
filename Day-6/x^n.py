num=int(input("Enter the base: "))
pow=int(input("Enter the power: "))

n=1
for i in range(pow):
    n=n*num
    
print(num,"to the power",pow,":",n)
    