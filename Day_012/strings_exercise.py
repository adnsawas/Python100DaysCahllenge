x = "Please, I want {} sandwishes and {} donutes"

# Replace 'I' with 'we'
x = x.replace("I", "we")

# Fill the blanks with 5 and 7
x = x.format(5, 7)

# Convert every 'a' to 'A'
x = x.replace('a', 'A')

print(x)