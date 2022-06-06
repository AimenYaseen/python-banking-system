from Account import Account
from Transaction import Transcation

class Bank():
    accounts = {}
    transcation = {}
    # accounts = {'pin':Customers()}
    # Transection_history = {'pin':[Transcation(), Transcation(), Transcation()]}

    def __init__(self):
        # Get the choice of user
        print("**********************************")
        print("\t\tWelcome to the Bank")
        print("**********************************")

        while True:
            try:
                print("\n***********************************\n")
                print("1. Create Account")
                print("2. Display Accounts")
                print("3. Deposit Amount")
                print("4. Withdraw Amount")
                print("5. Transfer Amount")
                print("6. Transaction History of specific account")
                print("7. Transaction History")
                print("8. Exit")
                print("\n***********************************\n")
                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    print("Enter the following Details to create your account")
                    # account = Account()
                    Bank.accounts[f"{Account.account_number - 1}"] = Account()

                elif user_choice == 2:
                    self.account_details()

                elif user_choice == 3:
                    Bank.accounts[f"{Account.account_number  - 1}"].deposit()
                
                elif user_choice == 4:
                    Bank.accounts[f"{Account.account_number  - 1}"].withdraw()

                elif user_choice == 5:
                    while True:
                        try:
                            if(len(Bank.accounts) >= 2):
                                receiver = int(input("Enter the receiver account number : "))
                                balance = Bank.accounts[f"{Account.account_number  - 1}"].balance
                                print(balance)
                                r_balance = Bank.accounts[f"{receiver}"].balance
                                print(r_balance)
                                if str(receiver) in Bank.accounts:
                                    if(receiver != Account.account_number - 1):
                                        print(f"Your current balance is {balance}")
                                        amount = int(input("Enter the amount to transfer : "))
                                        if(amount > 0 and amount <= balance):
                                           balance -= amount
                                           r_balance += amount
                                           print(f"Congratulations! Rs.{amount} has transfered to {receiver} account")
                                           print(f"Receiver account balance is {r_balance}")
                                           print(f"Now your current balance is {balance}")
                                           break
                                        else:
                                            print("You entered the wrong input")

                                    else:
                                        print("You can't send money to yourself")
                                        continue
                                else:
                                    print("Receiver does not exists")
                            else:
                                 print("You must have two accounts in order to transfer money")
                                 break
                        except (RuntimeError, TypeError, NameError, ValueError): 
                              print("***************************")
                              print("ERROR!")
                              print("Please Enter Valid Fields.  Try again...") 

                elif user_choice == 6:
                    acc_num = input("Enter the account number for transaction history : ")
                    self.transaction_history_specific(acc_num)
                
                elif user_choice == 7:
                    self.transaction_history()

                elif user_choice == 8:
                    print("Thankyou! for visiting our bank. Have a great day")
                    break

                else:
                    print("You entered the wrong input, Try Again")
                    continue

            except (RuntimeError, TypeError, NameError, ValueError): 
                 print("***************************")
                 print("ERROR!")
                 print("Please Enter Valid Fields.  Try again...")  

    def account_details(self):
        if(len(Bank.accounts)):
            print("*************************************")
            print("Accounts in the banks are: ")
            print(Bank.accounts)         
        else:
            print("***************************")
            print("ERROR!")
            print("There are no accounts yet, Please create an account first")

    def transaction_history(self):
        if(len(Bank.transcation)):
             print("***************************")
             print("ERROR!")
             print("There are no transactions yet, Please create a transaction first")
        else:
            print("*************************************")
            print("Transactions of ")
            print(Bank.transcation)

        
    def transaction_history_specific(self, account_number):
        if(not len(Bank.transcation)):
             print("***************************")
             print("ERROR!")
             print("There are no transactions yet, Please create a transaction first")
        elif account_number not in Bank.transcation:
             print("***************************")
             print("ERROR!")
             print(f"There are no transactions of this account # {Bank.account_number} yet, Please create a transaction first")
        else:
            print("*************************************")
            print("Transactions of account {}")
            print(Bank.transcation[f"{account_number}"])