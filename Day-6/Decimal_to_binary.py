num=int(input("Enter the decimal number: "))

i=0
bin=[]
while(num>0):
    rem=num%2
    num=num//2
    bin.append(rem)
    i=i+1

for k in range(i,0,-1):
    print(bin[k-1],end="")
