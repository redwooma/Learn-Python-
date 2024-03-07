# if statement : executes certain code when certain conditions are true, and other codes when other conditions are true.

is_male = True
is_tall = True



if is_male:
    # can put as much code in each if statement block
    print("You are a male.")
else:
    print("You are not a male.")

# can use the or operator
if is_tall and is_male:
    print("You are a male or tall or both.")
else:
    print("You are neither male nor tall.")

# can use the and operator
if is_tall and is_male:
    print("You are a tall male.")
# not function negates whatever is inside of here. Turns false to true and true to false.
elif is_male and not(is_tall):
    print("You are a short male.")
elif is_tall and not(is_male):
    print("You are a not a male, but are tall.")
else:
    print("You are not a male and are no tall.")
