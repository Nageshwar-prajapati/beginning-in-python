str=input("Enter the string: ")

vowel=0
cons=0
for ch in str:
    ch=ch.lower()
    if ch.isalpha():
        if( ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
            vowel+=1

        else:
            cons+=1

print("Vowel: ",vowel)
print("Consonent: ",cons)