#write functions here, don't add input('') statements here!

# Create a function that asks the user to enter a series of 5 numbers
def get_user_data():
    my_list = []


    for i in range(5):
        my_temp_num = int(input("Please enter 5 integers you would like to check \n"))
        my_list.append(my_temp_num)

    return my_list

# Create a function that grabs the LOWEST number in a list
def grab_lowest_nums(list):
    list.sort()
    return list[0]

# Create a function that grabs the HIGHEST number in a list
def grab_highest_nums(list):
    list.sort()
    return list[-1]

# Create a function that grabs the total numbers in a list
def grab_total_nums(list):
    sum = 0

    for nums in list:
        sum += nums

    return sum

# Create a function that grabs the AVERAGE numbers in a list
def grab_avg_nums(sum, list):
    total_nums = 0 
    
    for nums in list:
        total_nums += 1

    average = sum / total_nums

    return average