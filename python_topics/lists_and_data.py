# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.

fruits = [] # empty list
fruits = ["orange","apple","grape"]
print(fruits)

letters = list("python")
print(letters)

numbers = list(range(10))
print(numbers)

car_data = ["ferrari","f8",420000,2020,2900,"New York", True]
print(car_data)

# list items are indexed, the first item has index [0].
print(fruits[0], fruits[-1], sep=" ")

# nested lists.
sample = [[1, "a", 2], ["b", 3, 4], [6, 5, "c"]]
print(sample[0][1])
print(sample[-1][-1])

# list slicing (list_name[ Initial : End : IndexJump ]).
sample = ["p","y","t","h","o","n"]
print(sample[2:])
print(sample[:2])
print(sample[1:3])
print(sample[0:3:2])
print(sample[::])
print(sample[::-1])

# working with itens inside a list.
car_brands = ["ferrari","porsche","lamborghini"]

for index, brand in enumerate(car_brands):
    print(f"{index}: {brand}")

# list comprehension.
numbers = [1, 30, 21, 2, 9, 65, 34]
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)

numbers = [1, 30, 21, 2, 9, 65, 34]
evens = [number for number in numbers if number % 2 ==0]
print(evens)

squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)