class BankAccount:
    """
    This class represents a simple bank account.
    """

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Adds money to the account.
        """
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        """
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Not enough balance")

    def show_balance(self):
        """
        Prints the current balance.
        """
        print("Current balance:", self.balance)


# creating object
account = BankAccount("Alice", 1000)

# calling methods
account.show_balance()
account.deposit(500)
account.withdraw(300)
account.show_balance()
account.withdraw(2000)
