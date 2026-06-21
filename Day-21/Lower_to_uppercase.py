str=input("Enter the string: ")

str1=""

for ch in str:
    if 'a'<=ch <='z':
        str1+=chr(ord(ch)-32)

    else:
        str1+=ch

print("Uppercase String: ",str1)