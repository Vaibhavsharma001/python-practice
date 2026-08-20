# Create a BankAccount class containing:

# account_holder
# balance

# Create the following methods:

# Deposit(amount)

# Add money to the balance.
# Don't allow a negative deposit.

# Withdraw(amount)

# Subtract money from the balance.
# Don't allow withdrawal greater than the balance.
# Don't allow negative withdrawal.

# Show_balance()

# Display the current balance.
# Take the account details from the user and create the object.

# Give the user a menu:

# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit

# Challenge: Keep the menu running until the user chooses Exit.

#-------------------------------------------------------------------------------------|

class BankAccount:
    def __init__(self,account_holder,balance,digits):
        self.account_holder= account_holder
        self.balance= balance
        self.digits = digits
    def Deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"successfully deposited: {amount}")
        else:
            print("deposit amount must be positive")
            
    def Withdraw(self,amount):
        if amount>self.balance:
            print(f"failed: insufficient balance. Current balance--{self.balance}")
        elif amount<=0:
            print("withdrawal amount must be positive")
        else:
            self.balance-=amount
            print(f"successfully deducted: {amount} in your bank account ending with {self.digits}")
            
    def Show_balance(self):
        print(f"\n--- ACCOUNT DETAILS---")
        print(f"Holder:{self.account_holder}")
        print(f"Current Balance: {self.balance}")
        print("----------------------------")
        
object1 = BankAccount(
    input("enter account holder name:--"),
    int(input("enter your balance:--")),
    int(input("enter bank account's last four digits:--"))
)

while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter your deposit: "))
        object1.Deposit(amount)

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        object1.Withdraw(amount)

    elif choice == 3:
        object1.Show_balance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
        
#------------------------------------------------------------------------------------------|
# BankAccount OOP Practice

### What I practiced:

# * Created a `BankAccount` class.
# * Used `__init__()` to initialize account details.
# * Practiced `self` and object attributes.
# * Created `deposit()`, `withdraw()`, and `show_balance()` methods.
# * Added validation for negative deposits/withdrawals and insufficient balance.
# * Used a `while` loop to create a continuously running menu.

# ### OOP Concepts:
# **Class → Object → Constructor → Attributes → Methods → `self`**

# This practice helped me understand how OOP can be used to model a real-world bank account.
