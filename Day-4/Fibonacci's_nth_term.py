num=int(input("Enter the term: "))

first=0
sec=1

for i in range(num-1):
    next=first+sec
    first=sec
    sec=next
    
print("Nth term of series:",first)