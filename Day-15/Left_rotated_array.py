n=int(input("Enter the size of array: "))
arr=[]

print("Enter the elements of array: ")
for i in range(n):
    m=int(input(f"Enter {i+1} element "))
    arr.append(m)

left=int(input("Enter the number of left rotation: "))

for i in range(left):
    for j in range(n-1):
        temp=arr[j]
        arr[j]=arr[j+1]
        arr[j+1]=temp

print("Left rotated array: ",arr)