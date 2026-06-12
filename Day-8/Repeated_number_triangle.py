num=int(input("Enter the number of rows: "))
i=1
for k in range(num):
    for j in range(k+1):
        print(i,end="")
    i=i+1
    print("")