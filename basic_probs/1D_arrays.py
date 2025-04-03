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
# # to find min and max from the array
# def minmx():
#     arr = []

#     for i in range(0,4):
#         arr.append(int(input(f"enter the element {i + 1} : ")))

#     mn = arr[0]
#     mx = arr[0]

#     for i in range(0,4):
#         if arr[i] < mn :
#             mn = arr[i]
#         if arr[i] > mx :
#             mx = arr[i]

#     print(mn)
#     print(mx)

# minmx()
# ------------------------------------------------------------------------------

# # Array basics 3:
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
#     return arr_test

# nums=[2,1,3,0]
# perm = arr(nums)

# print("Input array:", nums)
# print("permutation array :" , perm)

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

# # alt method :
# def test(nums):
#     for i in range(1,len(nums)):
#         nums[i] += nums[i-1]
#     return nums

# nums = [1,1,1,1]
# print(test(nums))   
    
# ------------------------------------------------------------------------------

# # Shuffle the array :
# def shuffle(nums):
#     # Initialize an empty list for the result
#     result = []
#     # find after which point x series ends and y series starts
#     n = len(nums)//2

#     # Loop through the first half and the second half of the array
#     for i in range(n):
#         # Append the element from the first half
#         result.append(nums[i])
#         # Append the corresponding element from the second half
#         result.append(nums[i+n])
        
#     return result

# # Example usage
# nums = [2,1,3,4]
# shuffled_array = shuffle(nums)

# print("Input array:", nums)
# print("Shuffled array:", shuffled_array)    

# ------------------------------------------------------------------------------ 
# def conc_array(nums):
#     ans = nums + nums
#     return ans

# nums = [1,2,1]
# print(conc_array(nums))

# # alt method :
# def test(nums):
#     n = len(nums)
#     ans = (2*n) * [0]
#     for i in range(n):
#         ans[i] = nums[i]
#         ans[i+n] = nums[i]
#     return ans

# nums = [1,2,1]
# print(test(nums))

# ------------------------------------------------------------------------------ 



