# Python supports the usual logical conditions from mathematics:
# equals (a == b)       not equals (a != b)
# less than (a < b)     less than or equal to (a <= b)
# greater than (a > b)  greater than or equal to (a >= b)

MINIMUM_AGE = 18
MAXIMUM_AGE = 65

age = int(input("Enter your age: "))

# if statement.
if age >= MINIMUM_AGE:
    print("You are allowed to drive")

# else statement.
if age >= MINIMUM_AGE:
    print("You are allowed to drive")
else:
    print(f"You are not allowed to drive, try again in {MINIMUM_AGE - age} years")

# else if statement.
if age >= MAXIMUM_AGE:
    print("Please, consult the DMV")
elif age >= MINIMUM_AGE:
    print("You are allowed to drive")
else:
    print(f"You are not allowed to drive, try again in {MINIMUM_AGE - age} years")


# shorthand if else statement.
status = "above" if (age >= MINIMUM_AGE) else "below"
print(f"You are {status} the required age to drive.")