# for loop that execute codes that loops over a different collection of items
# can be arrays, or letters inside a string.

for letter in "Giraffe Academy":
    print(letter)

# arrays
friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

# indexes
# start from 3 and stops at index 10
for index in range(3, 10):
    print(index)

# range can be used for arrays
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(index)


friends = ["Jim", "Karen", "Kevin"]
for index in range(5):
    print(friends[index])

# can use logic
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")