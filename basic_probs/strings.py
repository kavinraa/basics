# # method 1
# def checkIfPangram(sentence: str) -> bool:
#     # convert sentence to set, to get letters without duplicate
#     set_sent = set(sentence)

#     # Get the length of letters in the set 
#     unique_letters = len(set_sent)
    
#     # check if equal to 26, since english alphabets == 26
#     return (unique_letters) == 26
    
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# result  = checkIfPangram(sentence)
# print(result)

# --------------------------------------------------------------------------------------------------

# # method 2
# import string

# def check_if_pangram(sentence):\
#     # To get set of all english letters in lowercase
#     eng_letters = set(string.ascii_lowercase)

#     # To get a set of all letters in the sentence
#     set_sent = set(sentence)

#     # To check if all letters are present in the sentence 
#     return eng_letters.issubset(set_sent)

# sentence = "thequickbrownfoxjumpsoverthelazydog"
# result  = check_if_pangram(sentence)
# print(result)

# --------------------------------------------------------------------------------------------------

# def print_triangle_alphabet_pattern(N):
#     alphabet = 'A'  # Starting with 'A'
    
#     for i in range(1, N + 1):
#         for j in range(i):
#             print(chr(ord(alphabet) + j), end=' ')
#         print()

# # Example usage:
# N = 5
# print_triangle_alphabet_pattern(N)

# --------------------------------------------------------------------------------------------------

# def reverse_words_in_string(s: str) -> str:
#     # split the string into list of words
#     list_s = s.split()

#     # Reverse the words in the list
#     reversed_words = list_s[::-1]

#     # join the reversed words into a single string
#     reversed_string = ' '.join(reversed_words)

#     return reversed_string


# # Example usage:
# input_string = "Hello world this is Python"
# result = reverse_words_in_string(input_string)
# print(result)  # Output: "Python is this world Hello"

# --------------------------------------------------------------------------------------------------

def is_palindrome(s: str) -> bool:
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is the same forward and backward
    return cleaned_string == cleaned_string[::-1]

# Example usage:
test_string = "A man, a plan, a cana"
result = is_palindrome(test_string)
print(result)  # Output: True
