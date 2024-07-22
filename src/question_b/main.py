from question_b import Stock

# Create an instance of the Stock class to use later
my_stock = Stock("MYSTK", "MyStock")

def main_menu():
    print("1. Display stock purchase history")
    print("2. Exit")

def handle_menu_options():
    main_menu()

    # Initialize options
    option = 0

    while option != 2:
        option = int(input("Please select what you would like to do\n"))

        if option == 1:
            my_stock.stock_purchase_history()
    

def main():
    handle_menu_options()

if __name__ == "__main__":
    main()
  