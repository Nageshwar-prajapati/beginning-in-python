n=int(input("Enter the size of array: "))
arr=[]

print("Enter the elements of array: ")
for i in range(n):
    m=int(input(f"Enter {i+1} element "))
    arr.append(m)

tar=int(input("Enter the target sum: "))

for i in range(n):
    for k in range(i+1,n):
        if(arr[i]+arr[k]==tar):
            print(f"{arr[i],arr[k]}")
