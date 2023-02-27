def print_multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")


if __name__ == "__main__":
    num = int(input("Enter the number: "))
    print_multiplication_table(num)
    
