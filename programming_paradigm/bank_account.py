class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add money into the account."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw money if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print current balance nicely."""
        # Format with two decimal places to show cents (e.g. $250.00)
        print(f"Current Balance: ${self._account_balance:.2f}")
