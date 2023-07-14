# Python provides different ways of passing the arguments during the function call.
#Types of arguments:
#   Keyword-only argument -> fun_name(name = value)
#   Positional-only argument -> fun_name(value)

# Slashes and asterisks as parameter name -> If a parameter is a slash (/), it 
# signifies that the parameters on its left side are position-only and hence 
# cannot be called by name. If a parameter is a asterisk (*), it signifies that 
# the parameters between the / and the * may be positional or keyword 
# parameters. The parameters following the * are keyword-only parameters. 

def func(param1, param2, /, param3, *, param4, param5):
     print(param1, param2, param3, sep= ".")
     print(param4, param5)

# Error - func("python", "3", "1.19", "Hello", "World")
# Error - func(param1 = "python", param2 = "3", param3 = "1.19", param4 = "Hello", param5 = "World")
func("python", "3", "1.19", param4 = "Hello", param5 = "World!")
func("python", "3", param3 = "1.19", param4 = "Hello", param5 = "World!")

# A function can take multiple arguments, these arguments can be objects, 
# variables(of same or different data types) and functions. Python functions are 
# first class objects.

def shout(text): 
    return text.upper() 
    
print(shout('Hello')) 
    
yell = shout    
print(yell('Hello')) 