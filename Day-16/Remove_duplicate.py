n=int(input("Enter the size of array: "))
arr=[]

print("Enter the elements of array: ")
for i in range(n):
    m=int(input(f"Enter {i+1} element "))
    arr.append(m)

for i in range(n):
    duplicate=1
    for j in range(i):
        if(arr[i]==arr[j]):
            duplicate=0
            break

    if(duplicate):
        print(arr[i],end=' ')
        
            