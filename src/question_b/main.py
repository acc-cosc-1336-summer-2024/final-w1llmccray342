from question_b import Stock

still_running = True  

def main_menu():
    print("1. Display stock purchase history")
    print("2. Exit")

def handle_menu_options():
    main_menu()

    while option != 2:
        option = input("Please select what you would like to do\n")

        if option == 1:
            Stock.stock_purchase_history()
    

def main():
    handle_menu_options()

if __name__ == "__main__":
    main()
  