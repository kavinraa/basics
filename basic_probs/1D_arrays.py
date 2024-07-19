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

# # running sum of 1-D array

# def running_sum(nums):
#     ans = []
#     sum = 0
#     for num in nums:
#         sum += num
#         ans.append(sum)
#     return ans

# nums = [5, 2, 6, 4]
# result = running_sum(nums)

# print("Input array:", nums)
# print("Running sum array:", result)
    
# ------------------------------------------------------------------------------

# # Shuffle the array :
# def shuffle(nums, n):
#     # Initialize an empty list for the result
#     result = []

#     # Loop through the first half and the second half of the array
#     for i in range(n):
#         # Append the element from the first half
#         result.append(nums[i])
#         # Append the corresponding element from the second half
#         result.append(nums[n + i])

#     return result

# # Example usage
# nums = [2, 5, 1, 3, 4, 7]
# n = 3
# shuffled_array = shuffle(nums, n)

# print("Input array:", nums)
# print("Shuffled array:", shuffled_array)

# ------------------------------------------------------------------------------






