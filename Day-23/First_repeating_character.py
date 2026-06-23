string=input("Enter the string: ")
ch=""
n=len(string)
found=0
for i in range(n):
    for j in range(i+1,n):
        if string[i]==string[j]:
            ch=string[i]
            found=1
            break

if found==1:
    print("First repating character: ",ch)

else:
    print("No repeating character.")

