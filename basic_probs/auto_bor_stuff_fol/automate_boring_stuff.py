# # guess the number in certain attempts game
# import random

# secret_number = random.randint(1,10)
# print("take a guess between 1 to 10")

# for i in range(1,5):
#     guess = int(input())

#     if  guess < secret_number :
#         print ("guess is less")
#     elif guess > secret_number :
#         print("guess is high")
#     else :
#         break

# if guess == secret_number :
#     print(f"you have guessed correctly in {i} attempts")    
# else :
#     print(f"nope. the number i was thinking was {secret_number}")

# --------------------------------------------------------------------------

# import random, sys

# print('ROCK, PAPER, SCISSORS')

# # These variables keep track of the number of wins, losses, and ties.
# wins = 0
# losses = 0
# ties = 0

# while True: # The main game loop.
#     print(f"{wins} Wins, {losses} Losses, {ties} Ties")
#     while True: # The player input loop.
#         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#         playerMove = input()
#         if playerMove == 'q':
#             sys.exit() # Quit the program.
#         if playerMove == 'r' or 'p' or 's':
#             break # Break out of the player input loop.
#         print('Type one of r, p, s, or q.')

#     # Display what the player chose:
#     if playerMove == 'r':
#         print('ROCK versus...')
#     elif playerMove == 'p':
#         print('PAPER versus...')
#     elif playerMove == 's':
#         print('SCISSORS versus...')

#     # Display what the computer chose:
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = 'r'
#         print('ROCK')
#     elif randomNumber == 2:
#         computerMove = 'p'
#         print('PAPER')
#     elif randomNumber == 3:
#         computerMove = 's'
#         print('SCISSORS')

#     # Display and record the win/loss/tie:
#     if playerMove == computerMove:
#         print('It is a tie!')
#         ties = ties + 1
#     elif playerMove == 'r' and computerMove == 's':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'p' and computerMove == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 's' and computerMove == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'r' and computerMove == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 'p' and computerMove == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 's' and computerMove == 'r':
#         print('You lose!')
#         losses = losses + 1

# ------------------------------------------------------------------
# zigzag game  

# import time,sys
# indent = 0
# indent_increasing = True

# try :
#     while True :
#         print(" " * indent, end="")
#         print("*****")
#         time.sleep(0.2)

#         if indent_increasing:
#             # increase the number of spaces
#             indent = indent + 1
#             if indent == 3:
#                 # change directions
#                 indent_increasing = False
            
#         else:
#             # decrease the number of spaces
#             indent = indent - 1
#             if indent == 0 :
#                 # Change directions
#                 indent_increasing = True

# except KeyboardInterrupt :
#     SystemExit

# ------------------------------------------------------------------

# def collatz(number):
#     if number % 2 == 0:
#         result = (number//2)
#     else :
#         result = (3 * number + 1)
#     print(result)
#     return(result)

# # user input and loop
# try :  
#     number = int(input("enter the number : "))
#     while number != 1 :
#         number = collatz(number)
# except ValueError :
#     print("Please enter a valid integer.")

# ------------------------------------------------------------------

# Multiple Assignment to the list :  assign multiple variables with the values in a list in one line of code
# cat = ['fat', 'gray', 'loud']
# size, color, sound = cat

# ------------------------------------------------------------------

# enumerate : returns both the index and items in a list. To be used in a for loop
# syntax : for index, items in enumerate(x):

# ------------------------------------------------------------------

# The random module has a couple functions that accept lists for arguments. The random.choice() function will return a randomly selected item from the list. Enter the following into the interactive shell:

# >>> import random
# >>> pets = ['Dog', 'Cat', 'Moose']
# >>> random.choice(pets)

# ------------------------------------------------------------------

# The random.shuffle() function will reorder the items in a list. 
# This function modifies the list in place, rather than returning a new list. 

# >>> import random
# >>> people = ['Alice', 'Bob', 'Carol', 'David']
# >>> random.shuffle(people)
# >>> people
# ['Carol', 'David', 'Alice', 'Bob']

# ------------------------------------------------------------------
# List Methods:

# Finding a Value in a List with the index() Method :
# >>> spam = ['hello', 'hi', 'howdy', 'heyas']
# >>> spam.index('hello')
# 0

# Append :
# The previous append() method call adds the argument to the end of the list

# >>> spam = ['cat', 'dog', 'bat']
# >>> spam.append('moose')
# >>> spam
# ['cat', 'dog', 'bat', 'moose']

# insert :
# The insert() method can insert a value at any index in the list. 
# The first argument to insert() is the index for the new value, 
# and the second argument is the new value to be inserted. 

# spam = ['cat', 'dog', 'bat']
# spam.insert(1, 'chicken')
# spam
# ['cat', 'chicken', 'dog', 'bat']

# Notice that the code is spam.append('moose') and spam.insert(1, 'chicken'), not 
# spam = spam.append('moose') and spam = spam.insert(1, 'chicken'). 
# Neither append() nor insert() gives the new value of spam as its return value. 
# (In fact, the return value of append() and insert() is None, 
# so you definitely wouldn’t want to store this as the new variable value.) Rather, the list is modified in place

# remove :
# The remove() method is passed the value to be removed from the list it is called on.
# spam = ['cat', 'bat', 'rat', 'elephant']
# spam.remove('bat')
# ['cat', 'rat', 'elephant']

# If the value appears multiple times in the list, only the first instance of the value will be removed

# Sorting the Values in a List with the sort() Method :
# Lists of number values or lists of strings can be sorted with the sort() method.

# >>> spam = [2, 5, 3.14, 1, -7]
# >>> spam.sort()
# >>> spam
# [-7, 1, 2, 3.14, 5]

# >>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
# >>> spam.sort()
# >>> spam
# ['ants', 'badgers', 'cats', 'dogs', 'elephants']

# You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order.

# >>> spam.sort(reverse=True)
# >>> spam
# ['elephants', 'dogs', 'cats', 'badgers', 'ants']

# Sort method Rules: 
# 1. First, the sort() method sorts the list in place;
# don’t try to capture the return value by writing code like spam = spam.sort().
# 2. you cannot sort lists that have both number values and string values in them.
# 3. uppercase letters come before lowercase letters. 
# Therefore, the lowercase a is sorted so that it comes after the uppercase Z.

# If you need to sort the values in regular alphabetical order, pass str.lower 
# for the key keyword argument in the sort() method call.

# >>> spam = ['a', 'z', 'A', 'Z']
# >>> spam.sort(key=str.lower)
# >>> spam
# ['a', 'A', 'z', 'Z']

# If you need to quickly reverse the order of the items in a list, 
# you can call the reverse() list method.

# >>> spam = ['cat', 'dog', 'moose']
# >>> spam.reverse()
# >>> spam
# ['moose', 'dog', 'cat']

# import random

# messages = ['It is certain',
#     'It is decidedly so',
#     'Yes definitely',
#     'Reply hazy try again',
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply is no',
#     'Outlook not so good',
#     'Very doubtful']

# print(messages[random.randint(0, len(messages) - 1)])

# spam = 42
# cheese = spam
# spam = 100
# print(spam)
# print(cheese)
# print(id(spam))
# print(id(cheese))
# print(id(100))
# print(id(42))

# --------------------------------------------------------------------------------
# Dictionary : 

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')
# -----------------------------------------------------

# spam = {'color': 'red', 'age': 42}
# for v in spam.values():
#     print(v)

# likewise : spam.key() gives 'key' in the dictionary, 'items' gives key and value pairs in the dictionary

# spam = {'color': 'red', 'age': 42}
# for k, v in spam.items():
#     print('Key: ' + k + ' Value: ' + str(v))

# spam = {'color': 'red', 'age': 42}
# print(list(spam.keys()))
# ---------------------------------------------------------------------------------------

# The get() Method : 
# dictionaries have a get() method that takes two arguments: the key of the value to retrieve 
# and a fallback value to return if that key does not exist.

# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# # 'I am bringing 2 cups.'
# print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# # 'I am bringing 0 eggs.

# ---------------------------------------------------------------------------------------
# The setdefault() Method :
#  The first argument passed to the method is the key to check for, 
# and the second argument is the value to set at that key if the key does not exist

# spam = {'name': 'Pooka', 'age': 5}
# >>> spam.setdefault('color', 'black')
# 'black'
# >>> spam
# {'color': 'black', 'age': 5, 'name': 'Pooka'}
# >>> spam.setdefault('color', 'white')
# 'black'
# >>> spam
# {'color': 'black', 'age': 5, 'name': 'Pooka'}

# The first time setdefault() is called, the dictionary in spam 
# changes to {'color': 'black', 'age': 5, 'name': 'Pooka'}. 
# The method returns the value 'black' because this is now the value set for the key 'color'. 
# When spam.setdefault('color', 'white') is called next, the value for that key is not changed to 'white', 
# because spam already has a key named 'color'.

# # pretty print : - The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists 
# or dictionaries and sorts the keys

# import pprint
# x = "hola aloh"
# count = {}
# for char in x :
#     count.setdefault(char,0)
#     count[char] = count[char] + 1
# pprint.pprint(count)

# If you want to obtain the prettified text as a string value instead of displaying it on the screen, call pprint.pformat() instead
# --------------------------------------------------------------------------------------

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':
# ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#          turn = 'X'
# printBoard(theBoard)

# -----------------------------------------------------------------------------------

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#              'Bob': {'ham sandwiches': 3, 'apples': 2},
#              'Carol': {'cups': 3, 'apple pies': 1}}

# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought

# print('Number of things being brought:')
# print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

# ----------------------------------------------------------------------------------

# Escape Characters
# print('Say hi to Bob\'s mother.')

# print("Hello there!\nHow are you?\nI\'m doing fine.")

# ----------------------------------------------------------------------------------

# # Raw Strings
#  A raw string completely ignores all escape characters and prints any backslash 
# that appears in the string. Raw strings are helpful if you are typing string values that contain many backslashes 
# such as the strings used for Windows file paths like r'C:\Users\Al\Desktop' or regular expressions

# print('That is Carol\'s cat.')
# ----------------------------------------------------------------------------------

'''Justifying Text with the rjust(), ljust(), and center() Methods'''
# def printpic(dict_items,right_w,left_w):
#     print("PIC".center(left_w +right_w, '*'))
#     for k,v in dict_items.items():
#         print(k.ljust(left_w, '-') + str(v).rjust(right_w, '-'))


# pic_items = {"apples" : 12, "oranges" : 10 , "bananas" : 11 }
# printpic(pic_items,5,5)
# ------------------------------------------------------------------------------ 