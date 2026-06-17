n=int(input("Enter the size of array: "))
arr=[]

for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr.append(m)

j=0
for i in range(n):
    if(arr[i]!=0):
        arr[j]=arr[i]
        j+=1

while(j<n):
    arr[j]=0
    j+=1

print("Array: ",arr)
