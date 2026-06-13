num=int(input("Enter the rows: "))
flag=64
for i in range(1,num+1):
    flag+=1
    for k in range(i):
        print(chr(flag),end="")
    print("")