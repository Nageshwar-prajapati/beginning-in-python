n=int(input("Enter the size of first array: "))
arr=[]

for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr.append(m)

k=int(input("Enter the size of second array: "))
arr2=[]

for i in range(k):
    m=int(input(f"Enter {i+1} element: "))
    arr2.append(m)

print("Common element(s): ",end="")
for i in range(n):
    for j in range(k):
        if(arr[i]==arr2[j]):
            print(arr[i],end=" ")