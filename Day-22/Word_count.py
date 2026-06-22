string=input("Enter the string: ")
count=0
n=len(string)
for i in range(n):
    if((i==0 and string[i]!=" ") or (string[i]==" " and string[i-1])):
        count+=1

print(f"Word in the string: {count}")