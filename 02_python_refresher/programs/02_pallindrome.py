# Write a function to check if a number is a pallindrome or not
def reverse_num(num):
    temp = 0
    while (num > 0):
        rem = num % 10
        temp = temp * 10 + rem
        num = num // 10
    print("Reversed number: ", temp)
    return temp

def check_pallindrome(num):
    return num == reverse_num(num)

if __name__ == "__main__":
    num = int(input("Enter the number: "))
    if (check_pallindrome(num)):
        print("Pallindrome")
    else:
        print("Not a pallindrome")
