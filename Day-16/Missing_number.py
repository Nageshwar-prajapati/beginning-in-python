n=int(input("Enter the size of array: "))
arr=[]

print("Enter the elements of array: ")
for i in range(n):
    m=int(input(f"Enter {i+1} element "))
    arr.append(m)

lar=int(input("Enter the largest number: "))
sum=0
for i in range(n):
    sum+=arr[i]

total=lar*(lar+1)//2
missnum=total-sum

print("MIssing number: ",missnum)