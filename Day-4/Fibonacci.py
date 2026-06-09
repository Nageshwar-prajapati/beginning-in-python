num=int(input("Enter the number of term:"))

first=0
sec=1

for i in range(num):
    print(first,end=' ')
    next=first+sec
    first=sec
    sec=next
    
