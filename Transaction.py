class Transcation:
    transaction_id = 1234
    def __iniy__(self, type, sender, amount,  receiver=""):
        if(type == "transfer"):
            self.receiver = receiver
        self.id = Transcation.transaction_id
        self.type=type
        self.account_holder = sender
        self.amount = amount

        Transcation.transaction_id +=1