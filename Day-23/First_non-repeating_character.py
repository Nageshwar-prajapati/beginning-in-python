string=input("Enter the string: ")
ch=""
n=len(string)
for i in range(n):
    count=0
    for j in range(i+1,n):
        if string[i]==string[j]:
            count+=1

    if count==0:
        ch=string[i]
        break

print("First non-repeating charcter: ",ch)
