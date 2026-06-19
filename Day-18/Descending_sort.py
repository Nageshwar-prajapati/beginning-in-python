n=int(input("Enter the size of array: "))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter {i+1} element: ")))

for i  in range(n-1):
    for j in range(n-1-i):
        if(arr[j]<arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print("Sorted array: ",arr)