# Write a function to get the second largest number in the given list
def get_second_largest(my_list, list_size):
    my_list.sort()
    return my_list[list_size-2]

if __name__ == "__main__":
    l = int(input("Enter the size of the list: "))
    my_list = []
    for i in range(l):
        temp = eval(input(f"Enter {i}th number: "))
        my_list.append(temp)

    print("Second largest of the list is ", get_second_largest(my_list, l))
    