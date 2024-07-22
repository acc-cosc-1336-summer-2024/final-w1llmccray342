#write functions here, don't add input('') statements here!
class Stock:
    
    # Create a constructor with symbol and company params.
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    # Create a method to return the symbol and company name, in this case we can just use the builtin __STR__ method to achieve
    # What we are trying to accomplish
    def __str__(self):
        return f"Stock Report \n{self.__symbol} \n{self.__company_name} "
