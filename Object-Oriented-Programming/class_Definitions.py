#Class --> Primary means for abstraction in OOP. In python every peice of data is represented as an instance of some class.

#Example Of Class --> Credit Card

class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """Creating a new credit card instance

        The initial balance is zero.

        customer  name of the customer
        bank      name of the bank
        acnt      account number
        limit     credit limit1
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Gives the name of the customer."""
        return self._customer

    def get_bank(self):
        """Gives the bank name."""
        return self._bank

    def get_account(self):
        """Return the card account number."""
        return self._account

    def get_limit(self):
        """Return the credit limit of the customer."""
        return self._limit

    def get_balance(self):
        """Gives the current balance of the customer."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return true if charge was processed; False if charge was denied."""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Akshat Rajvanshi', 'OP Bank', '1234 1234 1234 1234', 2500))
    wallet.append(CreditCard('Akshat Rajvanshi', 'TOPI Bank', '1234 1234 1234 4562', 5500))
    wallet.append(CreditCard('Akshat Rajvanshi', 'CHOTA Bank', '1234 1234 1234 7894', 8500))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(val*2)
        wallet[2].charge(val*3)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            print('New balance =', wallet[c].get_balance())
        print()