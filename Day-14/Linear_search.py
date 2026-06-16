n=int(input("Enter the size of array: "))
arr=[]

for i in range(n):
    m=int(input(f"Enter {i+1} element: "))
    arr.append(m)

targ=int(input("Enter the target element: "))

pos=-1
found=0
for i in range(n):
    if(arr[i]==targ):
        pos=i
        found=1
        break

if(found):
    print(f"Element found at {i+1} position.")

else:
    print("Element not found.")