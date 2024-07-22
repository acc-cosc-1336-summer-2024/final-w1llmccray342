class Stock:
    
    # Create a constructor with symbol and company params.
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    # Create a public method that returns the symbol
    def return_symbol(self):
        return self.__symbol

    # Create a public method that returns the company_name:
    def return_name(self):
        return self.__company_name
        
    def stock_purchase_history(self):
        # Create several pre-defined stocks
        apple_stk = Stock("AAPL", "Apple Inc")
        cate_stk = Stock("CAT", "Caterpillar")
        ek_stk = Stock("EK", "Eastman Kodak")
        google_stk = Stock("GOOG", "Google")
        msft_stk = Stock("MSFT", "Microsoft")

        # Add stocks to a temporary list
        temp_stocks = [apple_stk, cate_stk, ek_stk, google_stk, msft_stk]

        # Initialize an empty dictionary with my_stocks
        my_stocks = {}
        
        for stock in temp_stocks:
            my_stock_symbol = stock.return_symbol()
            my_stock_name = stock.return_name()

            my_stocks.update({my_stock_symbol: my_stock_name})
        
        for key, value in my_stocks.items():
            print (key, "\n", value)
