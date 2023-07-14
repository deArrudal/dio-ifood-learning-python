userlists = {
    "akun@mail.com": {"name": "john", "age": 25},
    "bkun@mail.com": {"name": "mike", "age": 18},
    "ckun@mail.com": {"name": "luke", "age": 31} 
}
print(userlists)

# {}.copy -> Returns a copy of the specified dictionary.
users = userlists.copy()
print(f"users: {users}")
      
# {}.clear -> Removes all the elements from a dictionary.
users.clear()
print(f"users: {users}")

# {}.fromkeys -> Returns a dictionary with the specified keys and the specified 
# value.
users = dict.fromkeys(["dkun@mail.com"])
print(f"users: {users}")

# {}.get -> Returns the value of the item with the specified key.
print(userlists.get("ckun@mail.com"))
print(userlists.get("dkun@mail.com"))

# {}.items -> Returns a view object. The view object contains the key-value pairs 
# of the dictionary, as tuples in a list.
print(userlists.items())

# {}.keys -> Returns a view object. The view object contains the keys of the 
# dictionary, as a list.
print(userlists.keys())

# {}.pop -> Removes the specified item from the dictionary.
userlists.pop("ckun@mail.com",{})
userlists.pop("dkun@mail.com",{})
print(userlists)

# {}.popitem -> Removes the item that was last inserted into the dictionary.
print(userlists.popitem())
print(userlists)

# {}.setdefault -> Returns the value of the item with the specified key.If the 
# key does not exist, insert the key, with the specified value
userlists.setdefault("akun@mail.com",{"name": "mike", "age": 18})
userlists.setdefault("bkun@mail.com",{"name": "mike", "age": 18})
print(userlists)

# {}.update -> Inserts the specified items to the dictionary.
userlists.update({"akun@mail.com":{"name": "john", "age": 28}})
print(userlists)

userlists.update({"ckun@mail.com": {"name": "luke", "age": 31} })
print(userlists)

# {}.values -> Returns a view object. The view object contains the values of the 
# dictionary, as a list.
print(userlists.keys())

# in -> Check if a item is inside a set.
print("dkun@mail.com" in userlists)
print("akun@mail.com" in userlists)

# del -> Delete the key that is present in the dictionary in Python
del userlists["bkun@mail.com"]["age"]
del userlists["ckun@mail.com"]
print(userlists)

