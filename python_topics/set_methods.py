set_a = {1, 2, 3}
set_b = {2, 3, 4}

print(set_a)
print(set_b)

# {}.union -> Returns a set that contains all items from the original set, and 
# all items from the specified set(s).
set_c = set_a.union(set_b)
print(set_c)

# {}.intersection -> Returns a set that contains the similarity between two or 
# more sets.
set_c = set_a.intersection(set_b)
print(set_c)

# {}.difference -> Returns a set that contains the difference between two sets.
set_c = set_a.difference(set_b)
print(set_c)

# {}.symmetric_difference -> Returns all the items present in given sets, except 
# the items in their intersections.
set_c = set_a.symmetric_difference(set_b)
print(set_c)

# {}.issubset() -> Returns True if set A is the subset of B, i.e. if all the 
# elements of set A are present in set B . Else, it returns False.
print(set_a.issubset(set_b))

# {}.issuperset() -> Returns True if all items in the specified set exists in the 
# original set, otherwise it returns False.
print(set_a.issuperset(set_b))

# {}.isdisjoint() -> Returns True if none of the items are present in both sets,
# otherwise it returns False.
print(set_a.isdisjoint(set_b))

# {}.add -> Adds one item to a set.
sample = {1, 23}
print(sample)

sample.add(42)
print(sample)

sample.add(42)
print(sample)

# {}.clear -> Removes all elements in a set.
sample.clear()
print(sample)

# {}.copy -> Copies the set.
sample = {1, 23}
print(sample)

new_sample = sample.copy
print(sample)

# {}.discard -> Removes the specified item from the set.
sample.discard(1)
print(sample)

# {}.pop -> Removes a random item from the set.
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numbers)

numbers.pop()
numbers.pop()
print(numbers)

# {}.remove -> Removes the specified element from the set.
numbers.remove(7)
print(numbers)

# len() -> Returns the number of elements in the list.
print(len(numbers)) 

# in -> check if a item is inside a set.
print(4 in numbers)