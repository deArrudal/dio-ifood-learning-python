sample = "HiRoShiMa, JaPaN"
print(sample)

# string in uppercase.
print(sample.upper())
# string in lowercase.
print(sample.lower())
# string in title format.
print(sample.title())

sample = "  Welcome to Brazil  "
print(sample)

# strip whitespaces from string
print(sample.strip())
# strip right whitespaces from string
print(sample.rstrip())
# strip left whitespaces from string
print(sample.lstrip())

title = "Python"
print("##" + title + "##")

# center align string, based on a given argument.
print(title.center(10))
print(title.center(10, "#"))

sample = "Abacate"

for letter in sample:
    print(letter + ".", end="")

print()
print(".".join(sample))