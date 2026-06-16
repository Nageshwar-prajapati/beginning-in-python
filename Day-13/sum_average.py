n=int(input("Enter the size of array: "))
arr=[]
sum=0
avg=0
print("Enter the elements of array: ")
for i in range(n):
    m=int(input(f"Enter {i+1} element "))
    arr.append(m)

print("Array:",arr)

for i in range(n):
    sum+=arr[i]

avg=sum/n

print("Sum of elements:",sum)
print("Average of elemets:",avg)

