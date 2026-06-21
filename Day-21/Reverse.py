str=input("Enter a string: ")

rev=""
for ch in str:
    rev=ch+rev

print("Reverse string:",rev)