num=int(input("Enter the number of rows: "))

ran=num+1
for i in range(1,ran):
    flag=0
    for j in range(ran-i):
        print(" ",end="")

    for k in range(i):
        flag+=1
        print(flag,end="")

    for m in range(i-1):
        flag-=1
        print(flag,end="")

    print("")