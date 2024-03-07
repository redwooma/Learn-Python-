# 2d list

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],
]

# first bracket is row
# second bracket is column
print(number_grid[2][1])

# nested for loop : a for loop in a for loop
for row in number_grid:
    for col in row:
        print(col)