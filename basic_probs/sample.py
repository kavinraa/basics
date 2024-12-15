# # find even or odd
# def odd_or_even(n):
#     if n%2 == 0 :
#         print(f"{n} is even")
#     else:
#         print(f"{n} is odd")

# (odd_or_even(38))

# ----------------------------------------------------------------------------------------------

# # Find the first digit and last digit of a number
# def firstDigit(n) : 
  
#     # Remove last digit from number till only one digit is left 
#     while n >= 10:  
#         n //= 10
      
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
#     # initialise po = 1
#     pow = 1
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
# divisor(100)

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

# check_if_prime_number(13)

# ----------------------------------------------------------------------------------------------

# def if_armstrong_number(n):     # sum of the digits raised to the number of digits == original number
#     # convert number to str for iteration 
#     digits = str(n)
#     # get the number of digits for power
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

# # Function to check Palindrome
# def check_palindrome(n):
#     reverse = 0
#     # Copy of the original number so that the original number remains unchanged while finding the reverse
#     temp = n
#     while temp != 0:
#         reverse = reverse * 10 + temp % 10
#         temp = temp // 10
#     # If reverse is equal to the original number, the
#     # number is palindrome
#     return reverse == n

# # Sample Input
# n = 12321
# if check_palindrome(n):
#       print("Yes")
# else:
#       print("No")

# # alt method
# def palindrome(n):
#     return str(n) == str(n)[::-1]

# print(palindrome(12321))

# ----------------------------------------------------------------------------------------------

# # Python3 program to find floor(sqrt(x)

# # Returns floor of square root of x


# def floorSqrt(x):
#     low = 1
#     high = x
#     while (low <= high) :
#         mid = (low + high) // 2
#         if (mid * mid) <= x :
#             low = mid + 1
#         else :
#             high = mid - 1
#     return high
# x = 10
# print(floorSqrt(x))

# ----------------------------------------------------------------------------------------------
