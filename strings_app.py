# working with strings

# Python \n : I want to print out a new line
# Python \" : I want to print out a quotation mark
# Concatenation : appending strings
# Function : a block of code that performs a specific operation to modify or get information about our string


phrase = "Giraffe Academy"

# .upper() method
# .lower() method
# .isupper() method : boolean
# .islower() method : boolean
print(phrase.upper().isupper())

# len() function
print(len(phrase))

# index
print(phrase[3])

# index() function : tells us where a specific character or number is in our string
# Returns where a word starts
# Returns an error if string is not found
print(phrase.index("Acad"))

# replace method
print(phrase.replace("Giraffe", "Elephant"))
