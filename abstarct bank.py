from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def payment_process():
        pass

class creditCard_payment(Payment):
    def payment_process(self):
        print("Processing via credit card...")
        
class payPal_payment(Payment):
    def payment_process(self):
        print("Processing via pay pal...")

class BankTransfer_payment(Payment):
    def payment_process(self):
        print("Processing via bank transfer...")

#creating instances
credit = creditCard_payment()
pay = payPal_payment()
bank = BankTransfer_payment()

credit.payment_process()
pay.payment_process()
bank.payment_process()
