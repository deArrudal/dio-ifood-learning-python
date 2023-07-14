# Tuples are used to store multiple items in a single variable. 
# A tuple is a collection which is ordered and unchangeable.

fruits = ("banana","apple","orange",)
sample = tuple("python")
numbers = ([4, 2, 3])

# to create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.
country = ("nigeria",)

print(fruits[1])
print(numbers[-1])

# nested tuples.
data = ((1, "a", 2),("b", 3, 4),(5, 6, "c"),)

print(data[0])
print(data[1][-1])