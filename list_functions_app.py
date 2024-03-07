lucky_numbers = [4, 8, 15, 16, 42, 23]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# adds the elements of lucky_numbers to friends
# adds two list together
friends.extend(lucky_numbers)
print(friends)

# add a element to a list
friends.append("Creed")
print(friends)

# inputs two parameter, index where you want to insert the parameter, and the name you want to add
# insert an element into an index of your list
friends.insert(1, "Kelly")
print(friends)

# remove an element from a list
friends.remove("Creed")
friends.remove(4)
friends.remove(8)
friends.remove(15)
friends.remove(16)
friends.remove(23)
friends.remove(42)
print(friends)

# remove everything from a list
# friends.clear()

# pop an item off a list
# removes the last item from a list
friends.pop()
print(friends)

# check if a specific element is in our list
# returns an error if element is not in a list
print(friends.index("Kevin"))

# count how many times an element occurs in a list
friends.append("Jim")
print(friends.count("Jim"))

# sort a list
# sort the list in ascending order
lucky_numbers.sort()
print(lucky_numbers)

# reverse a list
lucky_numbers.reverse()
print(lucky_numbers)

# copy a list
friends2 = friends.copy()
print(friends2)

