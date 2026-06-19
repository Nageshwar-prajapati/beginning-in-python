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
    arr3.append(arr1[i])

for i in range(k):
    found=1
    for j in range(n):
        if(arr2[i]==arr3[j]):
            found=0

    if(found==1):
        arr3.append(arr2[i])


print("Union of Array: ",arr3)