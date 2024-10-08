# # Find the first digit and last digit
# def firstDigit(n) : 
  
#     # Remove last digit from number till only one digit is left 
#     while n >= 10:  
#         n //= 10; 
      
#     # return the first digit 
#     return n

# def lastdigit(n):
#     n = n % 10

#     return n

# n = 98565
# print(firstDigit(n))
# print(lastdigit(n))  

# ----------------------------------------------------------------------------------------------

# def digit_count(n):
#     if n == 0 :
#         return 1

#     count = 0
#     while n != 0:
#         n //= 10
#         count += 1

#     return count

# n = 3432
# # print(digit_count(n))

# ----------------------------------------------------------------------------------------------

# def reverse_array_extra_array(arr):
#     reversed_arr = arr[::-1]
    
#     # Print reversed array
#     print("Reversed Array:", end=" ")
#     for i in reversed_arr:
#         print(i, end=" ")

# # Example usage:
# original_arr = [1, 2, 3, 4, 5]
# # reverse_array_extra_array(original_arr)

# ----------------------------------------------------------------------------------------------

# def reverse_number(n):
#     # Convert the number to a string, reverse it, handle negative sign
#     if n < 0:
#         reversed_num = -int(str(n)[:0:-1])
#     else:
#         reversed_num = int(str(n)[::-1])
#     return reversed_num

# # Example usage
# number = -12345
# reversed_number = reverse_number(number)
# print(reversed_number)  # Output will be -54321

# ----------------------------------------------------------------------------------------------

# def power(x,n):
#     # initialise power = 1
#     pow = 1
#     # multiply x for n times
#     for _ in range(n):
#         pow *= x
#     return pow

# x = 2
# n = 3

# print(power(x,n))

# ----------------------------------------------------------------------------------------------

# Python program to find GCD of two numbers


# Function to find gcd of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))

