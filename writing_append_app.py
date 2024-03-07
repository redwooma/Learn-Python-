# writing and appending a file

# adding text to the end of the file
# employee_file = open("employees.txt", "a")

# it will override the entire file and it's going to put this inside the file
employee_file = open("employees.txt", "w")

# can create a new file with "w"
employee_file = open("employees1.txt", "w")

# create an html file
employee_file = open("index.txt", "w")

# can write something to the end of the file
employee_file.write("<p>This is HTML</p>")

employee_file.close()