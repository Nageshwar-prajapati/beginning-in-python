def sum_of_digit(num):
    sum=0
    if(num==0):
        return 0

    if(num>0):
        return (num%10)+sum_of_digit(num//10)
        

num= int(input("Enter the nuber: "))
print("Sum of digits:",sum_of_digit(num))