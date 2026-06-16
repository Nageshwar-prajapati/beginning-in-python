n=int(input("Enter the size of array: "))
arr=[]

for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr.append(m)

max=arr[i]
smax=arr[i]

for i in range(n):
    if(arr[i]>max):
        max=arr[i]

for i in range(n):
    if(arr[i]<max and arr[i]>smax):
        smax=arr[i]

print(f"Second largest element: {smax}")