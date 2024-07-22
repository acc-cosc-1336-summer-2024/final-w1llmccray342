from question_c import question_c


def main_menu():
    print("1. Generate total and average data")
    print("2. Exit")

def handle_menu_options():

    # Initialize options
    option = 0

    while option != 2:
        main_menu()
        option = int(input("Please select what you would like to do\n"))

        if option == 1:
            my_data = question_c.get_user_data()
            my_lowest_number = question_c.grab_lowest_nums(my_data)
            my_highest_number = question_c.grab_highest_nums(my_data)
            my_total_number = question_c.grab_total_nums(my_data)
            my_avg_number = question_c.grab_avg_nums(my_data)

            print(f"The lowest number is... {my_lowest_number}")
            print(f"The highest number is... {my_highest_number}")
            print(f"The total is... {my_total_number}")
            print(f"The average is... {my_avg_number}")
        
        elif option == 2:
            print("Goodbye!")
    

def main():
    handle_menu_options()

if __name__ == "__main__":
    main()
  