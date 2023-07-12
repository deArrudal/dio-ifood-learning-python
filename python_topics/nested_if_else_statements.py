# if statements inside if statements are called nested if statements.

account_type = 0
balance = 2000
withdraw = 250
limit = 450

if account_type == 0:
    if(balance >= withdraw):
        print("Transaction successful")
    elif withdraw <= (balance + limit):
        print("Transaction successful, available limit used.")
    else:
        print("Insufficient balance")

elif account_type == 1:
    if(balance >= withdraw):
        print("Transaction successful")
    else:
        print("Insufficient balance")

else:
    print("Invalid account")