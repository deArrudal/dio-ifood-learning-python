# A function is a block of code which only runs when it is called. You can pass 
# data, known as parameters, into a function. A function can return data as a 
# result.

def my_fun():
    print("Hello from a function!")

# calling a function.
my_fun()

# sending an argument.
def my_fun_name(name = "anon"):
    print(f"Hello {name.title()}, i'm a function!")

my_fun_name()
my_fun_name("george")

# returning a parameter.
def between_number(number = 1):
    return number-1, number+1

print(between_number())
print(between_number(4))

# keyword arguments.
def display_car(model, brand, year, color):
    print(f"Car's data:\nBrand: {brand}\nModel: {model}\nYear: {year}\nColor: {color}")

display_car("Focus", "Ford", 1991, "Red") # correct input
display_car("Focus", 1991, "Red", "Ford") # wrong order
display_car(model = "Focus", year = 1991, color = "Red", brand = "Ford") # keywords


# arbitrary arguments (*args) -> If you do not know how many arguments that will 
# be passed into your function, add a * before the parameter name in the function 
# definition. This way the function will receive a tuple of arguments, and can 
# access the items accordingly
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# arbitrary keyword Arguments (**kwargs) -> If you do not know how many keyword 
# arguments that will be passed into your function, add two asterisk: ** before 
# the parameter name in the function definition. This way the function will 
# receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His first name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes") 
