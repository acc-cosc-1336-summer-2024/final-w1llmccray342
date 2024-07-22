#add import

from question_d import create_multiplication_table, display_multiplication_table

my_table_to_display = create_multiplication_table()

def main_menu():
    print("1. Display multiplication table")
    print("2. Exit")

def handle_menu_options():

    # Initialize options
    option = 0

    while option != 2:
        main_menu()
        try:
            option = int(input("Please select what you would like to do\n"))

        except ValueError:
            print ("ERROR: Please enter an INTEGER option.")
            continue

        if option == 1:
            display_multiplication_table(my_table_to_display)
        
        elif option == 2:
            print("Goodbye!")
    

def main():
    handle_menu_options()

if __name__ == "__main__":
    main()
  