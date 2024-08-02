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

# def flipAndInvertImage(image):
#     # iterate through each rpw in the input matrix
#     for row in image:
#         # flip the row horizontally by reversing it
#         row.reverse()
#         # invert the row 
#         for i in range(len(row)):
#             row[i] = 1 - row[i]
#     return image

# A = [
#     [1,1,0],
#     [1,0,1],
#     [0,0,0]
#     ]

# result = flipAndInvertImage(A)
# print("Result:")
# for row in result:
#     print(row)

# ---------------------------------------------------------------------------------------------

# Matrix Diagonal Sum

# def diagonalSum(mat):
#     n = len(mat)
#     total = 0
    
#     for i in range(n):
#         # Add the primary diagonal elements
#             total += mat[i][i]
#         # Add the primary diagonal elements
#             total += mat[i][n-i-1]
    
  
#     # If the matrix size is odd, subtract the middle element once
#     if n % 2 == 1:
#         total -= mat[n // 2][n // 2]
    
#     return total

# # Example usage
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(diagonalSum(matrix)) 

# ---------------------------------------------------------------------------------------------

# def find_odd_cells(matrix):
#     odd_cells = []

#     # Iterate over the rows and columns of the matrix
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] % 2 != 0:
#                 odd_cells.append((i, j))
    
#     return odd_cells

# # Example usage
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# odd_cells = find_odd_cells(matrix)
# print("Cells with odd values:", odd_cells)

# ---------------------------------------------------------------------------------------------
