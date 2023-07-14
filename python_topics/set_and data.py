# Sets are used to store multiple items in a single variable. A set is a 
# collection which is unordered, unchangeable*, and unindexed.
numbers = {1, 2, 3, 4, 5}
print(numbers, type(numbers), sep="; ")

print(set([1, 2, 3, 1, 3, 4]))
print(set("abacaxi"))
print(set(("ferrari", "porsche", "lamborghini")))

# access data.
sample = {1,2,3,2,4,4,6}
print(sample)

sample = list(numbers)
print(sample)
print(sample[3])

# iteration
numbers = {1,2,3,2,4,4,6}

for index, number in enumerate(numbers):
    print(f"{index}: {number}") 