num=int(input("Enter the number of rows: "))

for k in range(num):
    i=1
    for j in range(k+1):
        print(i,end="")
        i= i+1
    print("")