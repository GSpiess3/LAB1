# first file
class account:
    """
    A class designed to get info on a persons account
    """

    def __init__(self, name, balance=0) -> None:
        """
        To get the initial information.
        :param name: accounts name
        :param balance: accounts balance
        """
        self.__name = name
        self.__balance = balance

    def deposite(self, amount):
        if amount <= 0:
            return False
        else:
            self.__balance = amount + self.__balance
            return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False
        else:
            self.__balance = self.__balance - amount
            return True

    def get_name(self) -> str:
        """
        Get the accounts name
        :return: accounts name
        """
        return self.__name

    def get_balance(self) -> float:
        """
        Get the account balance
        :return: accounts balance
        """
        return self.__balance


