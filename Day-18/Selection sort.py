n=int(input("Enter the size of array: "))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter {i+1} element: ")))

for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if(arr[min]>arr[j]):
            min=j

    temp=arr[i]
    arr[i]=arr[min]
    arr[min]=temp

print("Sorted Array: ",arr)