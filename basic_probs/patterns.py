# # pattern1:
# def pattern1():
#     n = int(input("enter the number of loops : "))
#     for _ in range(n):
#         print ('* ' * n)

# pattern1()
# -----------------------------------------------------------------------------------------

# # Pattern2 - Loop to print stars incrementally in each row
# def pattern2():
#     n = int(input("enter the number of loops : "))
#     for i in range(1, n+1):
#         print ('* ' * i)

# pattern2()
# -----------------------------------------------------------------------------------------

# # pattern3 : Loop to print the number in right-angled triangle (dynamic - from inner loop)

# def pattern3():
#     n = int(input("enter the number of loops : "))
#     for i in range(1, n+1):
#         for j in range(1,i+1): 
#             print (j, end=" ")
#         print()

# pattern3()
# -----------------------------------------------------------------------------------------

# # pattern4 : Loop to print the number in right-angled triangle (static - from outer loop)
# def pattern4():
#     n = int(input("enter the number of loops : "))
#     for i in range(1, n+1):
#         for _ in range(1,i+1):
#             print (i, end=" ")
#         print()   

# pattern4()
# -----------------------------------------------------------------------------------------

# # pattern5: Loop to print inverted right-angled triangle of stars
# def pattern5():
#     n = int(input("enter the number of loops : "))
#     for i in range(n, 0, -1):
#         for _ in range(i):
#             print('*', end=' ')
#         print()

# pattern5()
# -----------------------------------------------------------------------------------------

# # pattern6: Loop to print inverted right-angled triangle of numbers:
# def pattern6():
#     n = int(input("enter the number of loops : "))
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print(j, end=" ")
#         print()

# pattern6()
# -----------------------------------------------------------------------------------------

# # pattern 7 : pyramid of stars
# def pattern7():
#     n = int(input("enter the number of loops : "))
#     for i in range(0,n):
#         # to print spaces
#         for _ in range(0,n-i-1):
#             print(" ", end="")
#         # to print stars 
#         for _ in range(0,2*i+1):
#             print("*",end="")
#         print()

# pattern7()
# -----------------------------------------------------------------------------------------

# # pattern8 : equilateral triangle - stars
# def pattern8():
#     n = int(input("enter the number of loops : "))
#     for i in range(0, 2*n-1):
#         stars = i + 1
#         if i >= n :
#             stars = 2*n - i - 1
#         for i in range(0, stars):
#             print("*", end =" ")
#         print()

# pattern8()
# -----------------------------------------------------------------------------------------


