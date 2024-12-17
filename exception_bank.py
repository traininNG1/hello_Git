class InsufficientBalanceException(Exception):
    def __init__(self, msg="insufficient balance to withdraw the specified amount"):
        super().__init__(msg)
class InvalidAmountException(Exception):
    def __init__(self, msg1="Deposit amount should be minimum $1"):
        super().__init__(msg1)


class Bank_account:
    def __init__(self,acc_holder,acc_num,balance=0):
        self.acc_holder = acc_holder
        self.acc_num = acc_num
        self.balance = balance

    #method for deposit
    def deposit(self):
        amount=int(input("Please enter the Deposit amount:"))
        try:
            if amount<=0:
                raise InvalidAmountException("Deposit amount must be greater than 1")
            self.balance+= amount
            print(f"Successfully deposited ${amount},available balance is : {self.balance}")
        except (InvalidAmountException) as a:
            print(f"Error:{a}")




    #method for withdraw money
    def money_withdraw(self):
        amount = int(input("Please enter the amonut to withdraw :"))
        try:
            if amount > self.balance:
                raise InsufficientBalanceException("Cannot withdraw more than your current balance.")
            self.balance-=amount
            print(f"{amount} withdadrawl successfull. Available balance is {self.balance}")
        except (InsufficientBalanceException) as e:
            print(f"Error:{e}")

    def dispay_accountDetails(self):
        print("<<<Account Details>>>")
        print("Name : ",self.acc_holder)
        print("Account Number :",self.acc_num)
        print("Account Balance :",self.balance)
a = Bank_account("Meera",7465423132344,balance=55600)
a.dispay_accountDetails()
a.deposit()
a.money_withdraw()
a.dispay_accountDetails()