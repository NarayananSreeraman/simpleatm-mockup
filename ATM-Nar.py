#PythonProgramToSimulateATMmachineNar
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount} successfully."
        else:
            return "Invalid amount for deposit."
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount} successfully."
        else:
            return "Invalid amount for withdrawal."
    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.account_holder}")
            return f"Transferred ${amount} to {recipient.account_holder} successfully."
        else:
            return "Invalid amount for transfer."
    def display_balance(self):
        return f"Current balance: ${self.balance}"
    def display_transaction_history(self):
        return "\n".join(self.transaction_history)
def main():
    # Create two bank accounts
    account1 = BankAccount(1234567890, 1000)#PIN=1234
    account2 = BankAccount(9876543210, 500)#PIN=5678
    print("Welcome to ABC BANK!")
    print("Please Enter your Account Number:")
    accnum=int(input())
    if(accnum==1234567890):
        print("Welcome, Ms.ANKSHITHA BHATTACHARJEE")
        print("Please enter your PIN:")
        pin1=int(input())
        if(pin1==1234):
            print("Login Successful!")
            while True:
                print("Please choose any one of the following options:")
                print("*** ATM Menu ***")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transfer")
                print("4. View Balance")
                print("5. Transaction History")
                print("6. Quit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    amount = float(input("Enter the deposit amount: "))
                    print(account1.deposit(amount))
                elif choice == "2":
                    amount = float(input("Enter the withdrawal amount: "))
                    print(account1.withdraw(amount))
                elif choice == "3":
                    recipient = account2
                    transacc=int(input("Enter the recipient's account number:"))
                    if(transacc==9876543210):
                        amount = float(input("Enter the transfer amount: "))
                        print(account1.transfer(recipient, amount))
                    else:
                        print("The Account Number you have entered does not exist.")
                elif choice == "4":
                    print(account1.display_balance())
                elif choice == "5":
                    print(account1.display_transaction_history())
                elif choice == "6":
                    print("Thank you for using our ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Try Again (1 Try Left)")
            pin2=int(input("Please enter your PIN:"))
            if(pin2==1234):
                print("Login Successful!")
                while True:
                    print("Please choose any one of the following options:")
                    print("*** ATM Menu ***")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. View Balance")
                    print("5. Transaction History")
                    print("6. Quit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        amount = float(input("Enter the deposit amount: "))
                        print(account1.deposit(amount))
                    elif choice == "2":
                        amount = float(input("Enter the withdrawal amount: "))
                        print(account1.withdraw(amount))
                    elif choice == "3":
                        recipient = account2
                        transacc=int(input("Enter the recipient's account number:"))
                        if(transacc==9876543210):
                            amount = float(input("Enter the transfer amount: "))
                            print(account1.transfer(recipient, amount))
                        else:
                            print("The Account Number you have entered does not exist.")
                    elif choice == "4":
                        print(account1.display_balance())
                    elif choice == "5":
                        print(account1.display_transaction_history())
                    elif choice == "6":
                        print("Thank you for using our ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Failed Attempt.")
        if(pin1!=1234):
            print("Thank you for using ABC Bank.")
    elif(accnum==9876543210):
        print("Welcome, Mr.ABHISHEK RAMAN")
        print("Please enter your PIN:")
        pin3=int(input())
        if(pin3==5678):
            print("Login Successful!")
            while True:
                print("Please choose any one of the following options:")
                print("*** ATM Menu ***")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transfer")
                print("4. View Balance")
                print("5. Transaction History")
                print("6. Quit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    amount = float(input("Enter the deposit amount: "))
                    print(account2.deposit(amount))
                elif choice == "2":
                    amount = float(input("Enter the withdrawal amount: "))
                    print(account2.withdraw(amount))
                elif choice == "3":
                    recipient = account1
                    transacc=int(input("Enter the recipient's account number:"))
                    if(transacc==1234567890):
                        amount = float(input("Enter the transfer amount: "))
                        print(account2.transfer(recipient, amount))
                    else:
                        print("The Account Number you have entered does not exist.")
                elif choice == "4":
                    print(account2.display_balance())
                elif choice == "5":
                    print(account2.display_transaction_history())
                elif choice == "6":
                    print("Thank you for using our ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Try Again (1 Try Left)")
            pin4=int(input("Please enter your PIN:"))
            if(pin4==5678):
                print("Login Successful!")
                while True:
                    print("Please choose any one of the following options:")
                    print("*** ATM Menu ***")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. View Balance")
                    print("5. Transaction History")
                    print("6. Quit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        amount = float(input("Enter the deposit amount: "))
                        print(account2.deposit(amount))
                    elif choice == "2":
                        amount = float(input("Enter the withdrawal amount: "))
                        print(account2.withdraw(amount))
                    elif choice == "3":
                        recipient = account1
                        transacc=int(input("Enter the recipient's account number:"))
                        if(transacc==1234567890):
                            amount = float(input("Enter the transfer amount: "))
                            print(account2.transfer(recipient, amount))
                        else:
                            print("The Account Number you have entered does not exist.")
                    elif choice == "4":
                        print(account2.display_balance())
                    elif choice == "5":
                        print(account2.display_transaction_history())
                    elif choice == "6":
                        print("Thank you for using our ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Failed Attempt.")
        if(pin3!=1234):
            print("Thank you for using ABC Bank.")
    else:
        print("Please enter the correct account ID.")
if __name__ == "__main__":
    main()