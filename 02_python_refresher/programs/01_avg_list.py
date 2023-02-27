# Write a function to calculate the average of numbers in the given list
def get_list_avg(my_list, list_size):
    sum = 0
    for i in my_list:
        sum = sum + i

    avg = sum / list_size
    return avg

if __name__ == "__main__":
    l = int(input("Enter the size of the list: "))
    my_list = []
    for i in range(l):
        temp = eval(input(f"Enter {i}th number: "))
        my_list.append(temp)

    print("Average of the list is ", get_list_avg(my_list, l))