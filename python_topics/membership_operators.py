# membership operators are used to test if a sequence
# is presented in an object.

fruits = ["banana","apple","pineapple"] 

# "in" returns True if a sequence with the specified value is present in the object.
print("lemon" in fruits)
print("apple" in fruits)
print("Banana" in fruits) # case sensitive

# "not in" returns True if a sequence with the specified value is not present in the object.
print("lemon" not in fruits)

# e.g.:
data = "coding in python is fun"
print( "python" in data)