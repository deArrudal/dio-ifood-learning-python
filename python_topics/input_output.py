# Syntax: input(prompt)
name = input("Name: ")
print(name)

age = input("Age: ")
print(f'Age = {age}, type = {type(age)}')

# Syntax: print(object(s), sep=separator, end=end, file=file, flush=flush)
# object(s) will be converted to string before printed.
# sep='separator' specify how to separate the objects, if there is more than one.
# end='end' specify what to print at the end.
# file define an object with a write method.
# flush define a Boolean, specifying if the output is flushed or buffered. 
print(name, age) # default
print(name, age, sep = '#') # separate objects using '#'
print(name, age, end = ";\n") # end print with semicolon and line feed

