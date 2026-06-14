def fibonacci(n):
    first,sec=0,1
    for i in range(n):
        print(first,end=' ')
        next=first+sec
        first=sec
        sec=next

num=int(input("Enter the number of terms: "))

print("Fibonacci series: ")
fibonacci(num)