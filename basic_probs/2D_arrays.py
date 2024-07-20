# creating 3*4 matrix :

# initializing empty matrix
mat = []

# getting user input for the matrix
for i in range(3):
    row = []
    for j in range(4):
        element = int(input(f"enter the element for row {i+1}, column {j+1} : "))
        row.append(element)
    mat.append(row)

# printing the matrix
print("3*4 matrix : ")
for row in mat:
    print(row)

