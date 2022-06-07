from Account import Account
from Transaction import Transcation

class Bank():
    accounts = {}
    transcation = {}
    # accounts = {'pin':Customers()}
    # Transection_history = {'pin':[Transcation(), Transcation(), Transcation()]}

    def __init__(self):
        # Get the choice of user
        print("**********************************************************")
        print("\t\tWelcome to the Bank")
        print("**********************************************************")

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
                    if str(Account.account_number -1) in Bank.accounts:
                        Bank.transcation[f"{Account.account_number - 1}"] = [] 
                        print("Success")                    

                # display accounts
                elif user_choice == 2:
                    self.account_details()

                # deposit money
                elif user_choice == 3:
                    if(len(Bank.accounts)):
                        result = Bank.accounts[f"{Account.account_number  - 1}"].deposit()
                        # print(result)
                        if(result[1] == True):
                            type = "deposit"
                            sender = str(Account.account_number-1)
                            amount = result[0]
                            Bank.transcation[f"{Account.account_number - 1}"].append(Transcation(type, sender, amount))
                    else:
                        print("Currently, You don't have any account")

                # withdraw money
                elif user_choice == 4:
                     if(len(Bank.accounts)):
                         result = Bank.accounts[f"{Account.account_number  - 1}"].withdraw()
                         if(result[1] == True):
                            type = "withdraw"
                            sender = str(Account.account_number-1)
                            amount = result[0]
                            Bank.transcation[f"{Account.account_number - 1}"].append(Transcation(type, sender, amount))
                     else:
                        print("Currently, You don't have any account")

                # transfer money
                elif user_choice == 5:
                    if(len(Bank.accounts)):
                        self.transfer_money()
                    else:
                        print("Currently, You don't have any account")

                # transaction history of specific account
                elif user_choice == 6:
                    self.transaction_history_specific()
                
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
                                        
                                           type = "transfer money"
                                           sender = str(Account.account_number  - 1)
                                           # creating transaction history
                                           Bank.transcation[f"{Account.account_number - 1}"].append(Transcation(type, sender, amount, str(receiver)))
                                           break
                                        else:
                                            print("You entered the wrong input")

                                    else:
                                        print("You can't send money to yourself")
                                        print("1. Back to menu \n2. Continue")
                                        check = int(input("Enter the number : "))
                                        if(check == 1):
                                            break
                                        elif(check == 2):
                                            continue
                                        else:
                                            print("You entered the wrong input")
                                else:
                                    print("Receiver does not exists, Try Again")
                                    print("1. Back to menu \n2. Continue")
                                    check = int(input("Enter the number : "))
                                    if(check == 1):
                                        break
                                    elif(check == 2):
                                        continue
                                    else:
                                        print("You entered the wrong input")
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
            for key, trans in Bank.transcation.items():
                 print("********************************")
                 print(f"Transactions of Account # {key}")
                 print(trans)

#  ****************** TRANSACTION HISTORY OF SPECIFIC *******************************
        
    def transaction_history_specific(self):
        try:
            if(len(Bank.transcation)):
                account_number = input("Enter the account number for transaction history : ")

                if account_number not in Bank.transcation:
                     print("***************************")
                     print("ERROR!")
                     print(f"There are no transactions of this account # {account_number} yet, Please create a transaction first")
        
                else:
                     print("*************************************")
                     print(f"Transactions of account {account_number}")
                     for trans in Bank.transcation[f"{account_number}"]:
                         print("********************************")
                         if(len(trans)):
                             print(trans)
                         else:
                             print(f"There are no transactions of this account # {account_number} yet, Please create a transaction first")

            else:
                 print("***************************")
                 print("ERROR!")
                 print("There are no transactions yet, Please create a transaction first")

        except (RuntimeError, TypeError, NameError, ValueError): 
                print("***************************")
                print("ERROR!")
                print("Please Enter Valid Fields.  Try again...") 
                            