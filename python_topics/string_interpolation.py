# String interpolation is a process substituting values 
# of variables into placeholders in a string. 

name = "John"
age = 28
gpa = 3.14
major = "Engineer"

# %-formatting -> Strings in Python have a unique built-in
# operation that can be accessed with the % operator.
print("Name: %s\nAge: %d\nGPA: %f.2\nMajor: %s" % (name, age, gpa, major))
print()

# Str.format() -> In this string formatting we use format()
# function on a string object and braces {}, the string object
# in format() function is substituted in place of braces {}.
print("Name: {0}\nAge: {1}\nGPA: {2}\nMajor: {3}".format(name, age, gpa, major))
print()

print("Name: {name}\nAge: {age}\nGPA: {gpa}\nMajor: {major}"
      .format(name = name, age = age, gpa = gpa, major = major))                                                                    
print()

# f-strings -> Python 3.6 added new string interpolation method 
# called literal string interpolation and introduced a new literal 
# prefix f.
print(f"Name: {name}\nAge: {age}\nGPA: {gpa}\nMajor: {major}")
print()

print(f"Name: {name}\nAge: {age}\nGPA: {gpa: .1f}\nMajor: {major}")
