class Acc:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def display(self):
        print(f"Name: {self.name}")
        print(f"Account: {self.acc_no}")
        print(f"Balance: {self.__balance}")

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print(f"{amt} is successfully added!")
        else:
            print("Invalid amount!")

    def withdraw(self, amt):
        if amt <= self.__balance and amt > 0:
            self.__balance -= amt
            print(f"Successfully {amt} is withdrawn")
        elif amt <= 0:
            print("Invalid amount!")
        else:
            print("Not sufficient balance!")

    def current_balance(self):
        print(f"{self.__balance} is the current balance")


name = input("Enter your name: ")
acc_no = input("Enter your Account no.: ")
user = Acc(name, acc_no, 1000)

while True:
    print("----Bank Account Management---")
    print("1.Display\n2.Deposit\n3.Withdraw\n4.Current Balance\n5.Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        user.display()

    elif choice == 2:
        try:
            amt = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        user.deposit(amt)

    elif choice == 3:
        try:
            amt = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        user.withdraw(amt)

    elif choice == 4:
        user.current_balance()

    elif choice == 5:
        print("Exiting the program.......")
        break

    else:
        print("Invalid choice. Choose 1-5.")
                        
         
        
                 
                       
            