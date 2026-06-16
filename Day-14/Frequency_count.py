n=int(input("Enter the size of array: "))
arr=[]

for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr.append(m)

targ=int(input("Enter the target element: "))

count=0
for i in range(n):
    if(arr[i]==targ):
        count+=1

if(count):
    print(f"Element {targ} have frequency: {count}")

else:
    print("Element not found.")