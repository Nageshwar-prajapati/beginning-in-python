string=input("Enter the string: ")

str=""
for ch in string:
    if(ch!=" "):
        str=str+ch


print("String after removing spaces:",str)
