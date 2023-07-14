languages = ("portuguese", "english", "french", "spanish", "japanese", "portuguese",)

# [].count -> Returns the number of elements with the specified value.
print(languages.count("portuguese"))


# [].index -> Returns the position at the first occurrence of the value.
print(languages.index("french"))

# len() -> Returns the number of elements in the list.
print(len(languages))

print(isinstance(languages, tuple))