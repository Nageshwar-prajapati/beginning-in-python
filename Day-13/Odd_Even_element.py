n=int(input("Enter the size of array: "))
arr=[]

for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr.append(m)

even=0
odd=0
for i in range(n):
    if(arr[i]%2==0):
        even+=1

    else:
        odd+=1


print("Even element:",even)
print("Odd element:",odd)