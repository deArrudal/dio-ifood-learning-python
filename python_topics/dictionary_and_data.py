# Dictionaries are used to store data values in key:value pairs. A dictionary is 
# a collection which is ordered*, changeable and do not allow duplicates.

user = {"name": "john", "age": 28}
print(user)

print(user["name"])

user["major"] = "science"
print(user)

car = dict(brand = "ford", model = "focus", year = 2002)
print(car)

# changing values.
user["name"] = "jane"
user["age"] = 19
user["major"] = "philosophy"
print(user)

# nested dictionaries.
userlists = {
    "akun@mail.com": {"name": "john", "age": 25},
    "bkun@mail.com": {"name": "mike", "age": 18},
    "ckun@mail.com": {"name": "luke", "age": 31} 
}

print(userlists["bkun@mail.com"]["age"])

# accessing data.
for key, value in userlists.items():
    print(f"{key}: \n\t{value}")