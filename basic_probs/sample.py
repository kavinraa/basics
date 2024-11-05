# # Find the first digit and last digit of a number
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
#         n = n // 10
#         count += 1
#     return count

# n = 23412
# print(digit_count(n))

# ----------------------------------------------------------------------------------------------

# def reverse_array_extra_array(arr):
#     reversed_arr = arr[::-1]
    
#     # Print reversed array
#     print("Reversed Array:", end=" ")
#     for i in reversed_arr:
#         print(i, end=" ")

# # Example usage:
# original_arr = [1, 2, 3, 4, 5]
# reverse_array_extra_array(original_arr)

# ----------------------------------------------------------------------------------------------

# def reverse_number(n):
#         # Reverse the string excluding the negative sign and add it back at the front
#     if n < 0:
#         reversed_num = -int(str(n)[:0:-1])
#     else:
#         # Reverse the string for positive numbers
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

# # Function to find gcd of two numbers
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd(48, 18))

# ----------------------------------------------------------------------------------------------

# # Print all divisors of a number
# def divisor(n):
#     i = 1
#     while i <= n :
#         if n % i == 0 :
#             print(i , end = ' ')
#         i = i + 1

# print ("The divisors of 100 are: ")
# divisor(10)

# ----------------------------------------------------------------------------------------------

# def check_if_prime_number(n):
#     counter = 0
#     for i in range(1, n+1):
#         if n % i == 0 :
#             counter += 1
#     if counter == 2 :
#         print("prime number")
#     else :
#         print("Not a prime number")

# check_if_prime_number(11)

# ----------------------------------------------------------------------------------------------

# def if_armstrong_number(n):     # sum of the digits raised to the number of digits == original number
#     # convert number to str for iteration
#     digits = str(n)
#     # get the number of digits 
#     power = len(digits)
#     #  get the sum of the number 
#     # total = sum(int(i) ** power for i in digits)
#     total = 0
#     for i in digits:
#         total += int(i) ** power

#     # check if total == original number
#     return total == n

# num = int(input("enter the number : "))
# if if_armstrong_number(num):
#     print(f"{num} is armstrong number")
# else :
#     print(f"{num} is not an armstrong number")

# ----------------------------------------------------------------------------------------------


