# Function with no argument and no return 
def print_hello():
    print("Hello")

# Function with no argument but some return value
def get_gravity_value():
    return 9.8

# Function with argument but no return
def log_value(num, default_val=3):
    print(f"Num: {num} Default Value: {default_val}")

# Function with arguments and return statement
def sum_numbers(num1, num2, num3):
    return num1 + num2 + num3


print_hello()
print(get_gravity_value())
log_value(4)
log_value(4, 5)
print(sum_numbers(6, 3, 8))
