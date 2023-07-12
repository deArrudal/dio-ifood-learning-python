# Python's default indentation spaces are four spaces.
# A minimum of one space is required to indent a statement.

def withdraw(amount):
    balance = 500

    if(balance >= amount):
        print("Transaction successful")
    else:
        print("Insufficient balance")

withdraw(100)
withdraw(1000)