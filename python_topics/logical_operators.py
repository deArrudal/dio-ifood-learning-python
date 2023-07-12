# Logical operators are used to combine conditional statements.
number_1 = 10
number_2 = 20
number_3 = 15
flag = True

# "and" returns True if both statements are true.
print(True and True)
print(True and False)
print(False and False)

# "or" returns True if one of the statements is true.
print(True or True)
print(True or False)
print(False or False)

# "not" reverses the result, returning False if the result is true.
print(not True)
print(not False)

# e.g.:
print(number_1 >= number_2 and number_2 <= number_3)
print(flag and number_2 > number_1)