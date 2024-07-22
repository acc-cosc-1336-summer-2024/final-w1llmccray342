#write functions here, don't add input('') statements here!
class Stock:
    
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def __str__(self):
        return f"Stock Report \n {self.__symbol} \n{self.__company_name} "
