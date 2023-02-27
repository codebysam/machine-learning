# While Loop to print series
curr_num = 0
max_num = int(input("Enter the number till which you want to print the series: "))

while (curr_num <= max_num):
    print(curr_num)
    curr_num = curr_num + 1


# For loop to print multiplication table
num = int(input("Enter the number for which the table has to be printed: "))

for i in range(11):
    print(f"{num} x {i} = {num*i}")


# For loop to iterate a list with their indexes
names_list = ["John", "Jane", "Janine"]

print("List items with their indexes")

for i, _name in enumerate(names_list):
    print(f"{i} - {_name}") 
    
