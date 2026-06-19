n=int(input("Enter the size of first array: "))
arr1=[]
for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr1.append(m)


k=int(input("Enter the size of first array: "))
arr2=[]
for i in range(k):
    m=int(input(f"Enter {i+1} element: "))
    arr2.append(m)


arr3=arr1+arr2

print("Merged Array: ",arr3)