# read txt. file, html. file, csv. file
# python read command

# r = read : read the information in the file
# w = write : can change the file and write new information
# a = append : you append information onto the end of the file
# r+ = read and write

employee_file = open("employees.txt", "r")
# check if the file is readable

print(employee_file.readable()) # returns a boolean value

#print(employee_file.readline()) # reads the first line
#print(employee_file.readline()) # reads the second line
#print(employee_file.readline()[1]) # can use index

for employee in employee_file.readlines():
    print(employee)

# close function : so we are no longer able to access it.
employee_file.close()

