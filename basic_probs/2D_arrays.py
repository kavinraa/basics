# creating 3*4 matrix :

# initializing empty matrix
# mat = []

# # getting user input for the matrix
# for i in range(3):
#     row = []
#     for j in range(4):
#         element = int(input(f"enter the element for row {i+1}, column {j+1} : "))
#         row.append(element)
#     mat.append(row)

# # printing the matrix
# print("3*4 matrix : ")
# for row in mat:
#     print(row)

# ---------------------------------------------------------------------------------------------

def flipAndInvertImage(image):
    # iterate through each rpw in the input matrix
    for row in image:
        # flip the row horizontally by reversing it
        row.reverse()
        # invert the row 
        for i in range(len(row)):
            row[i] = 1 - row[i]
    return image

A = [
    [1,1,0],
    [1,0,1],
    [0,0,0]
    ]

# result = flipAndInvertImage(A)
print("Result:")
for row in result:
    print(row)

# ---------------------------------------------------------------------------------------------
