# Identity operators are used to compare the objects, not if 
# they are equal, but if they are actually the same object, with
# the same memory location.

data_1 = 100
data_2 = 500

# "is" returns True if both variables are the same object
print(data_1 is data_2)

data_3 = data_1
print(data_1 is data_3)

data_4 = 500
print(data_2 is data_4)

# "is not" returns True if both variables are not the same object
print(data_1 is not data_2)


