num=int(input("Enter the number of rows: "))

ran=num+1
for i in range(ran,0,-1):
    for j in range(ran-i):
        print(" ",end="")

    for k in range(2*i-1):
        print("*",end='')
 
    print("")