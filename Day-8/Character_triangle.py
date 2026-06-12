num=int(input("Enter the rows: "))

for i in range(1,num+1):
    for k in range(i):
        print(chr(65+k),end="")
    print("")