def factorial(m):
    fac=1
    for i in range(1,m+1):
        fac=fac*i
    
    return fac

num=int(input("Enter tha number: "))
print("Factorial of",num,':',factorial(num))