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

                # create account
                if user_choice == 1:
                    print("Enter the following Details to create your account")
                    # account = Account()
                    Bank.accounts[f"{Account.account_number - 1}"] = Account()

                # display accounts
                elif user_choice == 2:
                    self.account_details()

                # deposit money
                elif user_choice == 3:
                    result = Bank.accounts[f"{Account.account_number  - 1}"].deposit()
                    if(result[1] == True):
                        type = "deposit"
                        sender = Account.account_number-1
                        amount = result[0]
                        #Bank.transcation[f"{Account.account_number  - 1}"].append(Transcation(type, sender, amount))

                # withdraw money
                elif user_choice == 4:
                     result = Bank.accounts[f"{Account.account_number  - 1}"].withdraw()
                     if(result[1] == True):
                        type = "withdraw"
                        sender = Account.account_number-1
                        amount = result[0]
                        Bank.transcation[f"{Account.account_number  - 1}"] = []
                        Bank.transcation[f"{Account.account_number  - 1}"].append(Transcation(type, sender, amount))

                # transfer money
                elif user_choice == 5:
                   self.transfer_money()

                # transaction history of specific account
                elif user_choice == 6:
                    acc_num = input("Enter the account number for transaction history : ")
                    self.transaction_history_specific(acc_num)
                
                # transaction history
                elif user_choice == 7:
                    self.transaction_history()

                # Exit
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
            
    # *************************** ALL ACCOUNTS IN BANK****************************

    def account_details(self):
        
        if(len(Bank.accounts)):
            print("*************************************")
            print("Accounts in the banks are: ")
            # print(Bank.accounts.values())
            for acc in Bank.accounts.values():
                print("********************************")
                print(acc)       
        else:
            print("***************************")
            print("ERROR!")
            print("There are no accounts yet, Please create an account first")

    # ************************ TRANSFER MONEY ******************************************

    def transfer_money(self):
         while True:
                        try:
                            if(len(Bank.accounts) >= 2):
                                receiver = int(input("Enter the receiver account number : "))
                             
                                # if receiver is present or not
                                if str(receiver) in Bank.accounts:
                                    if(receiver != Account.account_number - 1):
                                        balance = Bank.accounts[f"{Account.account_number  - 1}"].balance
                                        print(f"Your current balance is {balance}")

                                        # enter amount
                                        amount = int(input("Enter the amount to transfer : "))

                                        #validation
                                        if(amount > 0 and amount <= balance):
                                           Bank.accounts[f"{Account.account_number  - 1}"].balance -= amount
                                           Bank.accounts[f"{receiver}"].balance += amount

                                           r_balance = Bank.accounts[f"{receiver}"].balance
                                           balance = Bank.accounts[f"{Account.account_number  - 1}"].balance

                                           print(f"Congratulations! Rs.{amount} has transfered to {receiver} account")
                                           print(f"Receiver account balance is {r_balance}")
                                           print(f"Now your current balance is {balance}")
                                           break
                                        else:
                                            print("You entered the wrong input")

                                    else:
                                        print("You can't send money to yourself")
                                else:
                                    print("Receiver does not exists, Try Again")
                            else:
                                 print("You must have two accounts in order to transfer money")
                                 break
                        except (RuntimeError, TypeError, NameError, ValueError): 
                              print("***************************")
                              print("ERROR!")
                              print("Please Enter Valid Fields.  Try again...") 
                              break
 

    # ************************ TRANSACTION HISTORY **************************************

    def transaction_history(self):
        
        if(not len(Bank.transcation)):
             print("***************************")
             print("ERROR!")
             print("There are no transactions yet, Please create a transaction first")
        
        else:
            print("*************************************")
            print("Transactions of ")
            for trans in Bank.transcation.values():
                 print("********************************")
                 print(trans)

#  ****************** TRANSACTION HISTORY OF SPECIFIC *******************************
        
    def transaction_history_specific(self, account_number):

        if(not len(Bank.transcation)):
             print("***************************")
             print("ERROR!")
             print("There are no transactions yet, Please create a transaction first")

        elif account_number not in Bank.transcation:
             print("***************************")
             print("ERROR!")
             print(f"There are no transactions of this account # {account_number} yet, Please create a transaction first")
        
        else:
            print("*************************************")
            print(f"Transactions of account {account_number}")
            for trans in Bank.transcation[f"{account_number}"]:
                 print("********************************")
                 print(trans)