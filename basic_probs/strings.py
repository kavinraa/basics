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
