def create_multiplication_table():
    my_list = []

    # Create a multiplication table with 10 columns and 5 rows.
    # We create our First LIST by creating an empty list of 1-10 that we'll use to check each other list.
    # We can loop through my_list_A and the next list which will just be the values of my_list_a * the initial value of the next list
    my_list_a = []
    my_nums_to_check = [2, 3, 4, 5]

    # Create the initial list with a range of 10    
    for nums in range(10):
        my_list_a.append(nums+1)
    my_list.append(my_list_a)

    # Create an empty list for every number we are checking
    for num in my_nums_to_check:
        my_list_to_add = []

        # For each number in my_nums_to_check we multiply it by every number in my_list_a and save the result
        for nums in my_list_a:
            number_to_add_to_list = num * nums
            my_list_to_add.append(number_to_add_to_list)
        
        # We add the temporary list to a new variable.
        my_list.append(my_list_to_add)

    return my_list

def display_multiplication_table(list):
  for nums in list:
    print(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9])


    