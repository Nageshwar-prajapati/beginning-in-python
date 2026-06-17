n=int(input("Enter the size of array: "))
arr=[]

print("Enter the elements of array: ")
for i in range(n):
    m=int(input(f"Enter {i+1} element "))
    arr.append(m)

j=0
i=n-1
while(j<i):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i-=1
    j+=1

print("Reverse Array: ",arr)