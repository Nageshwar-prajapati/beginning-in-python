def reverse(num):
    if num < 10:
        return num

    digits = len(str(num)) - 1
    return (num % 10) * (10 ** digits) + reverse(num // 10)


num=int(input("Enter the number: "))
print("Reverse of number:",reverse(num))
