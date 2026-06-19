n=int(input("Enter the size of first array: "))
arr1=[]
for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr1.append(m)


k=int(input("Enter the size of second array: "))
arr2=[]
for i in range(k):
    m=int(input(f"Enter {i+1} element: "))
    arr2.append(m)

arr3=[]

for i in range(n):
    for j in range(k):
        if(arr1[i]==arr2[j]):
            arr3.append(arr1[i])

print("Intersection of Array: ",arr3)