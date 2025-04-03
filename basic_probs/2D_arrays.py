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

# ---------------------------------------------------------------------------------------------

# def flipAndInvertImage(image):
#     # iterate through each row in the input matrix
#     for row in image:
#         # flip the row horizontally by reversing it
#         row.reverse()
#         # invert the row : 1 -> 0 ; 0 -> 1
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
# Odd cells with indices : solution using row increments

# def oddCells(m, n, indices):
#     # create row and column increment
#     row_inc = [0]*m
#     col_inc = [0]*n

#     # apply the increment for each index
#     for r,c in indices:
#         row_inc[r] += 1
#         col_inc[c] += 1

#     # count the cells with odd values
#     odd_count = 0
#     odd_cells = []
#     for i in range(m):
#         for j in range(n):
#             # A cell (i, j) has an odd value if the sum of row and column increments is odd
#             if (row_inc[i] +col_inc[j]) % 2 == 1:
#                 odd_count += 1
#                 odd_cells.append((i,j))
#     print(f'The odd cells are : ', odd_cells)
#     return odd_count

# m = 2
# n = 3
# indices = [[0, 1], [1, 1]]
# result = oddCells(m, n, indices)
# print(f"Sum of cells with odd values:", result)  # Output: 6

# ---------------------------------------------------------------------------------------------

# Odd cells with indices : solution by directly modifying the matrix

# def oddCells(m, n, indices):
#     length = len(indices)

#     # Initialize a matrix of size m x n with all values set to 0
#     mat = [[0] * n for _ in range(m)]

#     # Apply the increments for each index in indices
#     for i in range(length):
#         row = indices[i][0]

#         # Increment all values in the row 'row' by 1
#         for k in range(n):  # Use 'n' because you want to increment across columns
#             mat[row][k] += 1

#         col = indices[i][1]

#         # Increment all values in the column 'col' by 1
#         for k in range(m):  # Use 'm' because you want to increment across rows
#             mat[k][col] += 1

#     # Count the number of cells with odd values
#     ans = 0
#     for i in range(m):
#         for j in range(n):
#             if mat[i][j] % 2 == 1:
#                 ans += 1

#     return ans  # Make sure to return the final answer

# # Example usage
# m = 2
# n = 3
# indices = [[0, 1], [1, 1]]
# result = oddCells(m, n, indices)
# print(f"Sum of cells with odd values: {result}")  # Output: 6

# ---------------------------------------------------------------------------------------------

# # transpose of a matrix : method 1
# def transpose(matrix):
#     # get the length of row and column of original matrix
#     row = len(matrix)
#     col = len(matrix[0])

#     # initialize a zero transpose matrix with col as rows & rows as col -> (col*row)
#     transpose_matrix = [[0]* col for _ in range(row) ]

#     # fill the tranpose matrix by swapping rows and cols
#     for i in range(row):
#         for j in range(col):
#             transpose_matrix [j][i] = matrix[i][j]
    
#     return transpose_matrix


# # Example usage
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transposed = transpose(matrix)

# print("original matrix : ")
# for row in matrix:
#     print(row)

# print("\ntransposed matrix :")
# for row in transposed:
#     print(row)

# ---------------------------------------------------------------------------------------------

# # transpose of a matrix : method 2
# def transpose(matrix):
#     trans_mat = zip(*matrix)
#     return trans_mat

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transposed = transpose(matrix)

# print("transpose_matrix : ")
# for row in transposed:
#     print(row)

# ---------------------------------------------------------------------------------------------

def maximumWealth(accounts):
    max_wealth = 0
    for i in range(len(accounts)):
        row_sum = 0
        for j in range(len(accounts[i])):
            row_sum += accounts[i][j]
        if row_sum > max_wealth :
            max_wealth = row_sum
    return max_wealth
    

# Test Case
accounts = [[1,5], [7,3], [3,5]]
print(maximumWealth(accounts))  # Output: 10