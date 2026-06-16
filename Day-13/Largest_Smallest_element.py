n=int(input("Enter the size of array: "))
arr=[]

for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr.append(m)

max=arr[i]
min=arr[i]

for i in range(n):
    if(arr[i]<min):
        min=arr[i]

    if(arr[i]>max):
        max=arr[i]

print("\nLargest element:",max)
print("Minimum element:",min)