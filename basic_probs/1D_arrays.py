# # Array basics 1:
# # Take space-separated input from the user
# input_string = input("Enter the elements separated by space: ")

# # Split the input string into a list of strings
# array = input_string.split()

# # Convert the list of strings to a list of integers
# # Using list comprehension with error handling
# try:
#     array = [int(x) for x in array]
# except ValueError:
#     print("Please enter valid integers.")
#     exit()

# # Print the resulting array
# print("Array:", array)

# ------------------------------------------------------------------------------

# # Array basics 2:
# n = 5
# array = [] 
# for i in range(n):
#     element = int(input(f"Enter element {i + 1}: "))
#     array.append(element)

# print(array)

# ------------------------------------------------------------------------------

# # # Array basics 3:
# # Using the array Module
# import array as arr

# # Prompt the user for the size of the array
# n = int(input("Enter the number of elements: "))

# # Initialize an empty array of integers
# array = arr.array('i', [])

# # Loop to collect inputs
# for i in range(n):
#     element = int(input(f"Enter element {i + 1}: "))
#     array.append(element)

# # Print the resulting array
# print("Array:", array)

# ------------------------------------------------------------------------------

# # build arrays from permutation :

# def arr(nums):
#     length = len(nums)
#     arr_test = []
#     for i in range(length):
#         arr_test.append(nums[nums[i]])
#     return arr

# nums=[2,0,3,1]
# perm = arr(nums)


# print("Input array:", nums)
# print("Permutation array:", perm)

# ------------------------------------------------------------------------------

# running sum of 1-D array

def running_sum(nums):
    length = len(nums)
    sum = 0
    for i in range(length):
        sum += nums[i]
        nums[i] = sum
    return nums

nums = [1, 2, 3, 4]
result = running_sum(nums)

print("Input array:", nums)
print("Running sum array:", result)
    
