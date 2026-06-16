n=int(input("Enter the size of array: "))
arr=[]

print("Enter the elements of array:")
for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr.append(m)

print("Duplicate element: ")
for i in range(n-1):
    duplicate=0
    for j in range(i+1,n):
        if(arr[i]==arr[j]):
            duplicate=1
            elem=arr[i]
            
    if(duplicate):
        print(arr[i],end=" ")
