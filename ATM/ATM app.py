#ATM project

print("Welcome to NSI bank ATM")

class ATM:
        def __init__(self, balance=1000):
            self.balance=balance
        
        def check_balance(self):
            return f"your account balance is ${self.balance}"
        
        def deposit(self, amount):
            self.balance += amount
            return f"Deposited ${amount}.Your new balance is ${self.balance}"
        
        def Withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdraw ${amount}.Your new balance is ${self.balance}"
            else:
                return "Insufficient balance. Withdraw failed !!!"
        

atm=ATM()
while True:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice =input("Enter your choice:")
    print("________---*---________")

    if choice == '1':
        print(atm.check_balance())
    elif choice == '2':
        amount = float(input("Enter your deposit amount:"))
        print(atm.deposit(amount))    
    elif choice =='3':
        amount = float(input("Enter your withdraw amount:"))
        print(atm.Withdraw(amount))
    elif choice =='4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")



    