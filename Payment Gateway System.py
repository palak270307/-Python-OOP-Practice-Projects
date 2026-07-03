from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, user, balance):
        self.user = user
        self.__balance = balance   # Encapsulation

    def deduct_balance(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
            return True
        else:
            return False

    @abstractmethod
    def pay(self, amt):
        pass


class UPI(Payment):
    def pay(self, amt):
        if self.deduct_balance(amt):
            print(f"{self.user} paid {amt} using UPI")
        else:
            print("Insufficient Amount")


class CreditCard(Payment):
    def pay(self, amt):
        if self.deduct_balance(amt):
            print(f"{self.user} paid {amt} using Credit Card")
        else:
            print("Insufficient Amount")


class Wallet(Payment):
    def pay(self, amt):
        if self.deduct_balance(amt):
            print(f"{self.user} paid {amt} using Wallet")
        else:
            print("Insufficient Amount")


print("--- Payment ---")
user = input("Enter User name: ")
balance = int(input("Enter balance amount: "))

print("1. UPI\n2. Credit Card\n3. Wallet\n4. Exit")
choice = int(input("Enter your choice: "))

if choice == 4:
    print("Exiting....")
else:
    amt = int(input("Enter Amount to pay: "))

    if choice == 1:
        p = UPI(user, balance)
    elif choice == 2:
        p = CreditCard(user, balance)
    elif choice == 3:
        p = Wallet(user, balance)
    else:
        print("Invalid Choice")
        exit()

    p.pay(amt)   # Important
                
                                                                    