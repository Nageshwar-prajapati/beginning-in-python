string=input("Enter the string: ")

targ=input("Enter the target character: ")

count=0
for ch in string:
    if(ch==targ):
        count+=1

print(f"Frequency of {targ}: {count}")