# first file
class Account:

    def __init__(self, name, balance = 0) -> None:
        """
        Constructor
        :param name: accounts name
        :param balance: account balance
        """
        self.__name = name
        self.__balance = balance

    def deposite(self, amount):
        """
        :param amount: amount to be deposited
        :return:
        """
        if amount <= 0:
            return False
        else:
            self.balance = amount + self.balance
            return True

    def withdraw(self, amount):
        """
        :param amount: amount to be withdrawn
        :return:
        """
        if amount <= 0 or amount > self.balance:
            return False
        else:
            self.balance = self.balance - amount
            return True

    def get_name(self) -> str:
        """
        To get the account name
        :return: account name
        """
        return self.__name

    def get_balance(self) -> float:
        """
        To get the account balance
        :return: account balance
        """
        return self.__balance