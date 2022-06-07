from sre_constants import SUCCESS


class Account:
    minimum_amount = 100
    account_number = 4301

    def __init__(self):
        try :
             name = input("Enter your name : ")
             gender = input("Enter your gender : ")
             pin = int(input("Enter your password pin (must be integer) : "))
             balance = int(input(f"Deposit some amount, it should be greater than {Account.minimum_amount} : "))

             # pin
             if pin < 0 or len(str(pin)) < 4 or len(str(pin)) > 4:
                 print("***************************")
                 print("ERROR!")
                 print("Pin should be greater than zero and its length should be equal to 4, Try Again")
                 # verified = False
                 return

             # amount
             if balance<Account.minimum_amount:
                 print("***************************")
                 print("ERROR!")
                 print(f"Your initial bank balance should be greater than {Account.minimum_amount}")
                 # verified = False
                 return

            # creating account
            # if(verified):
             self.name = name
             self.gender = gender
             self.pin = pin
             self.balance = balance
             self.account_number = Account.account_number

             #updating account number
             Account.account_number +=1
     
             print("******************************")
             print("\nCongratulations! Your bank account has created\n")  
             self.customer_detail() 

        except (RuntimeError, TypeError, NameError, ValueError): 
             print("***************************")
             print("ERROR!")
             print("Please Enter Valid Fields.  Try again...")
             return

    def customer_detail(self):
        print("*******************************************")
        print("\nBank Account Details")
        print(f"Account Number : {self.account_number}")
        print(f"Name : {self.name}")
        print(f"Gender : {self.gender}")
        print(f"Balance : {self.balance}")
        print(f"Account Pin : {self.pin}")

 # **************************** DEPOSIT ***********************************   
    def deposit(self):
        try:
            success = False
            print(f"Your current balance is {self.balance}")
            amount = int(input("Enter the amount to deposit : "))
            if(amount > Account.minimum_amount):
                self.balance += amount
                print(f"Congratulations! Rs.{amount} has added to your account")
                print(f"Now your current balance is {self.balance}")
                success = True
                return amount, success
            else:
                 print("***************************")
                 print("ERROR!")
                 print(f"Deposited amount should be greater than {Account.minimum_amount}")              

        except (RuntimeError, TypeError, NameError, ValueError): 
             print("***************************")
             print("ERROR!")
             print("Please Enter Valid Fields.  Try again...")  
 
 # **************************** WITHDRAW *********************************
    def withdraw(self):
        success = False
        try:
            print(f"Your current balance is {self.balance}")
            amount = int(input("Enter the amount to withdraw : "))
            if(amount > 0 and amount <= self.balance):
                self.balance -= amount
                print(f"Congratulations! Rs.{amount} has deducted from your account # {self.account_number}")
                print(f"Now your current balance is {self.balance}")
                success = True
                return amount, success
            else:
                print("***************************")
                print("ERROR!")
                print("You entered the wrong amount")   
        except (RuntimeError, TypeError, NameError, ValueError): 
             print("***************************")
             print("ERROR!")
             print("Please Enter Valid Fields.  Try again...")  

# *****************************TRNASFER MONEY ******************************
    # def transfer_money(self):
    #     try:
    #         sender = input("Enter the sender account number")

    #         amount = int(input("Enter the amount to withdraw : "))
    #     except (RuntimeError, TypeError, NameError, ValueError): 
    #          print("***************************")
    #          print("ERROR!")
    #          print("Please Enter Valid Fields.  Try again...")  
    
    def __repr__(self):
         return f"Account Number : {self.account_number} \n Name : {self.name} \n Gender : {self.gender} \n Balance : {self.balance} \n Account Pin : {self.pin}"