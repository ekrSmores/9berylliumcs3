class BankAccount:
    """Class"""
    def __init__(self, accountNumber: int, Balance: float):
        self.__accountNumber = accountNumber
        self.__Balance = Balance

    def set_account_number(self, Accounted):
        if type(Accounted) is int and Accounted >= 0:
            self.__accountNumber = Accounted
        else: 
            print("Account must ONLY have Positive WHOLE Numbers")

    def set_balance(self, Number):
        if Number >= 0: 
            self.__Balance = Number
        else:
            print("Reason: Balance can NOT be negative")

    def get_account_number(self):
        return f"Account No.: {self.__accountNumber}."

    def get_balance(self):                          
        return f"Balance: {self.__Balance}."


a1 = BankAccount(6767, 1000)
print(f"{a1.get_account_number()}")
print(f"Current {a1.get_balance()}")
print("Protection test(Encapsulation) \n _______________________________________________________________________________")
Setter = int(input("Update balance to: "))
a1.set_balance(Setter)
print(f"{a1.get_account_number()}")
print(f"Current {a1.get_balance()}")
