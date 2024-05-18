# pattern1:
def pattern1():
    n = int(input("enter the number of loops : "))
    for i in range(n):
        for j in range(n):
            print ("* ", end="")
        print()

# pattern1()

# # Number of rows and columns
# n = 5

# # Loop to print square star pattern
# for i in range(n):
#     print('* ' * n)

# # Pattern2
# # Number of rows
# rows = 5

# # Loop to print each row
# for i in range(1, rows + 1):
#     # Print 'i' stars
#     print('* ' * i)

def pattern2():
    n = int(input("enter the number of loops : "))
    for i in range(1, n+1):
        for j in range(i):
            print ("* ", end="")
        print()

# pattern2()

# pattern3
def pattern3():
    n = int(input("enter the number of loops : "))
    for i in range(1, n+1):
        for j in range(1,i+1):
            print (j, end=" ")
        print()

# pattern3()

# pattern4
def pattern4():
    n = int(input("enter the number of loops : "))
    for i in range(1, n+1):
        for j in range(1,i+1):
            print (i, end=" ")
        print()   

# pattern4()

