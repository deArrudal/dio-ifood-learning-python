# A for loop is used for iterating over a sequence (that is 
# either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming 
# languages, and works more like an iterator method as found 
# in other object-orientated programming languages.

sample = input("Insert a phrase: ")
vowels = "aeiou"

# for loop.
for letter in sample:
    if letter in vowels:
        print(letter, end = " ")

print()

# range.
# The range() function returns a sequence of numbers.
for number in range(0, 11, 2):
    print(number, end= " ")

print()

# while.
option = -1

while option != 0:
    option = int(input("[1] Test 1\n[2] Test 2\n[0] Exit\nEnter option: "))

    if option == 1:
        print("\tTest 1")
    elif option == 2:
        print("\tTest 2")
    else:
        print("\tERROR")


print("EXIT")

# keywords.
for number in range(21):
    if number % 3 == 0:
        continue # skip to next iteration.
    elif number == 19:
        break # break loop.
    else:
        print(number)