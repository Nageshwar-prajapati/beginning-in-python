str1=input("Enter the first string: ")
str2=input("Enter the second string: ")

if(len(str1)!=len(str2)):
    print("Not anagram")

else:
    flag=True

    for ch in str1:
        if(str1.count(ch)!=str2.count(ch)):
            flag=False

    if(flag):
        print("ANAGRAM")

    else:
        print("Not anagram")