class Transcation:
    
    def __init__(self):
         # Get the choice of user
        print("**********************************")
        print("\t\tLet's do some transaction")
        print("**********************************")

        while True:
            try:
                print("\n***********************************\n")
                print("1. Deposit Amount")
                print("2. Withdraw Amount")
                print("3. Transfer Amount")
                print("4. Exit")
                print("\n***********************************\n")
                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    self.deposit()

                elif user_choice == 2:
                    self.withdraw()

                elif user_choice == 3:
                    self.transfer_money()

                elif user_choice == 4:
                    print("Thankyou!")
                    break

                else:
                    print("You entered the wrong input, Try Again")
                    continue

            except (RuntimeError, TypeError, NameError, ValueError): 
                 print("***************************")
                 print("ERROR!")
                 print("Please Enter Valid Fields.  Try again...")  


    def deposit(self):
        try:
            amount = int(input("Enter the amount to deposit : "))

        except (RuntimeError, TypeError, NameError, ValueError): 
             print("***************************")
             print("ERROR!")
             print("Please Enter Valid Fields.  Try again...")  

    def withdraw(self):
        try:
            amount = int(input("Enter the amount to withdraw : "))
        except (RuntimeError, TypeError, NameError, ValueError): 
             print("***************************")
             print("ERROR!")
             print("Please Enter Valid Fields.  Try again...")  

    def transfer_money(self, sender):
        try:
            pass
        except (RuntimeError, TypeError, NameError, ValueError): 
             print("***************************")
             print("ERROR!")
             print("Please Enter Valid Fields.  Try again...")  
