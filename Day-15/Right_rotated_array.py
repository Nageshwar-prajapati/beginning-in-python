n=int(input("Enter the size of array: "))
arr=[]

print("Enter the elements of array: ")
for i in range(n):
    m=int(input(f"Enter {i+1} element "))
    arr.append(m)

right=int(input("Enter the number of right rotation: "))

for i in range(right):
    for j in range(n-1,0,-1):
        temp=arr[j]
        arr[j]=arr[j-1]
        arr[j-1]=temp


print("Right rotated array: ",arr)