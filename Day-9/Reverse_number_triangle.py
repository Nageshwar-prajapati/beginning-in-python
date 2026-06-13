num=int(input("Enter the number of rows: "))

for i in range((num),0,-1):
    flag=1
    for j in range(i):
        print(flag,end='')
        flag+=1

    print('')

