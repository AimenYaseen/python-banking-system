from importlib.util import set_loader


class Transcation:
    transaction_id = 1234
    def __init__(self, type="", sender="", amount=0,  receiver=""):
        # print("Transaction")
        self.receiver = receiver
        self.id = Transcation.transaction_id
        self.type=type
        self.account_holder = sender
        self.amount = amount

        Transcation.transaction_id +=1
    
    def __repr__(self):
         return f"\n(Transaction_id : {self.id} \n Transaction Type : {self.type} \n Account Holder : {self.account_holder} \n Receiver: {self.receiver} \n Amount Transfered : {self.amount})\n"