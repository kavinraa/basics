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


