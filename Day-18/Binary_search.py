n=int(input("Enter the size of array: "))
arr=[]
print("Enter the array in ascending sorting")
for i in range(n):
    arr.append(int(input(f"Enter {i+1} element: ")))

targ=int(input("Enter the target element: "))

beg=0
end=n-1
found=0
while(beg<=end):
    mid=(beg+end)//2
    if(arr[mid]==targ):
        print(f"Element found at {mid+1} position")
        found=1
        break

    elif(arr[mid]<targ):
        beg+=1
        
    else:
        end-=1

if(found==0):
    print("Element not found")
