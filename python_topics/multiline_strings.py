name = "thomas"
language = "french"

# multiline string.
message = f"""
Hello, my name is {name.title()}.
    Right now, I'm learning {language.title()}.
        Salut, my friends.
"""
print(message)


menu = """
    ====== MENU =====
    1. Withdraw
    2. Deposit
    0. Exit
    ================= 
"""
print(menu)