string=input("Enter the string: ")
ch=""
n=len(string)
count=0
for i in range(n):
    c=0
    for j in range(i,n):
        if string[i]==string[j]:
            c+=1

    if count<c:
        count=c
        ch=string[i]
        

print(f"Maximum occuring character {ch}: {count}")
