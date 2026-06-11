num=int(input("Enter the number: "))

while(num%2==0):
    primefac=2
    num=num//2

rang=int(num**0.5)+1
for i in range(3,rang):
    while(num%i==0):
        primefac=i
        num=num//i

if(num>2):
    primefac=num

print("Largest prime factor:",primefac)