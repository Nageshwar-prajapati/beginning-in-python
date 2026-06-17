n=int(input("Enter the size of array: "))
arr=[]

print("Enter the elements of array: ")
for i in range(n):
    m=int(input(f"Enter {i+1} element "))
    arr.append(m)

count=0
for i in range(n):
    tar=arr[i]
    c=0
    for j in range(n):
        if(arr[j]==tar):
            c+=1

    if(c>count):
        count=c
        num=tar

print(f"Maximum frequency element {num}: {count}")