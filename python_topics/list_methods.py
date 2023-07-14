# [].append -> Appends an element to the end of the list.
sample = []

sample.append(1)
sample.append("Python")
sample.append([30, 20, 40])
print(sample)

#[].clear -> Removes all items from the list.
sample.clear()
print(sample)

# [].copy -> Copy a List. In python, you cannot copy a list simply by typing 
# list2 = list1, because: list2 will only be a reference to list1, and changes 
# made in list1 will automatically also be made in list2.
sample_copy = sample
print(id(sample), id(sample_copy)) # same reference.

sample_copy = sample.copy()
print(id(sample), id(sample_copy)) # not the same reference.

# [].count -> Returns the number of elements with the specified value.
colors = ["red", "blue", "green", "blue", "red", "blue"]

print(colors.count("red"))
print(colors.count("green"))
print(colors.count("blue"))

# [].extend -> Adds all the elements of an iterable to the end of the list.
languages = ["french", "english", "japanese"]
new_languages = ["italian", "spanish", "portuguese"]

languages.extend(new_languages)
print(languages)

# [].index -> Returns the position at the first occurrence of the value.
print(languages.index("italian"))

# [].pop -> Removes the element at the specified position.
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruit = fruits.pop(1) 
print(fruits)
print(fruit)

# [].remove -> Removes the first occurrence of the specified item.
fruit = fruits.remove("cherry") 
print(fruits)

# [].reverse -> Reverses the elements of the list. 
fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits.reverse()
print(fruits)

# [].sort -> Sorts the list ascending by default. You can also make a function 
# to decide the sorting criteria(s).
fruits = ["apple", "mangoes", "banana", "cherry"]
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.sort(key=lambda x:len(x)) # sort by number of characters.
print(fruits)


# len() -> Returns the number of elements in the list.
print(len(fruits))

# sorted() -> Returns a sorted list of the specified iterable object.
print(fruits)
print(sorted(fruits, reverse = True))