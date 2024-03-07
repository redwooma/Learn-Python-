# dictionary is a special structure in Python which allows us to store important in key value pair.

# the word is a key or the word uniquely identifies it inside of the dictionary and then the value would be the actual definition.

# convert a three digit month name into the full month name.
# Jan -> January or Mar -> March

monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
# specify a default value

# you may put in a key and it does not necessarily map to a value inside of the dictionary so you put in an invalid key.
print(monthConversions.get("Luv", "Not a valid Key"))

# can use numbers for dictionaries 