# lab25-ATM.py

class ATM:
    """ A base ATM Class to get trans history, balance, dep, withdraw """  
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    # check current balance and add it to transaction history
    def check_balance(self):
        self.transaction_history.append(f"Balance check: ${self.balance}")
        return self.balance

    # deposit user amount and add it to balance
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(
            f"Deposit: ${amount} Balance: ${self.balance}"
        )
        return self.balance

    # check to see if a withdrawal would overdraft the account
    def check_withdrawal(self, amount):
        self.transaction_history.append(
            f"Check withdrawal: ${self.balance} - " +
            f"${amount} = {self.balance - amount}"
        )
        return self.balance - amount

    # withdraw user amount and remove from balance
    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_history.append(
            f"Withdrawal ${amount} -- Balance: ${self.balance}"
    )    

    # get transaction history
    def check_history(self):
        return [str(i) for i in self.transaction_history]



def main():
    # create new ATM object
     new_account = ATM()

     # things users can do
     valid_inputs = [
                     'd', 'deposit',
                     'w', 'withdraw',
                     'c', 'check balance',
                     't', 'test overdraw',
                     'h', 'history',
                     'e', 'exit'
                    ]

     print("Welcome to your new bank account!")

     while True:
        while True:
            command = input(
                "What would you like to do?" + "\n" +
                "(deposit\nwithdraw\ntest a withdrawal\n"+
                "exit\ncheck balance\nhistory) ").strip().lower()
            if command in valid_inputs:
                break
        if command.startswith("d"):
            dep = int(input("How much would you like to deposit?\n$"))
            new_account.deposit(dep)
            print(f"Your account is now ${new_account.check_balance()}")
        elif command.startswith("w"):
            wd = int(input("How much would you like to withdraw?\n$"))
            new_account.deposit(wd)
        elif command.startswith('c'):
            print(f"Your current balance is {new_account.check_balance()}")
        elif command.startswith('t'):
            twd = int(input("How much would you like to test for?\n$"))
            print(f"Your new balance would be {new.account.check_withdrawal(twd)}")
        elif command.startswith('h'):
            print("Here is your transaction history: ")
            history = new_account.check_history()
            for i in history:
                print(i)
        else:
            print("Goodbye!")
            break


main()

