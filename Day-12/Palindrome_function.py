def palindrome(num):
    n,rev=num,0
    while(n!=0):
        rem=n%10
        n=n//10
        rev=rev*10+rem

    return(rev==num)

num=int(input("Enter the number: "))

if(palindrome(num)):
    print("Palindrome")

else:
    print("Not palindrome")