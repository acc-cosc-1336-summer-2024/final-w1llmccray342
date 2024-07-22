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
        pass
