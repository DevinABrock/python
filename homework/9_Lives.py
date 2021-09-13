import random

### Rules ###
words = ["pizza", "fairy", "teeth", "shirt", "otter", "plane"]
game_board = [["?"], ["?"], ["?"], ["?"], ["?"]]
heart_symbol = u'\u2764'
life = 9
lives = heart_symbol * life
points = 0
print("You have nine lives. Can you guess the secret word?")

### Word Generator ###
secret_word = random.choice(words) #picks a random word from list
secret_word_list = list(secret_word) #makes the secret word into a list
print("The word has been chosen") # it works up to here

### Gameplay ###
while True:
    print(game_board)
    print(lives)
    user_input = input("guess a letter or type quit: ")
    if user_input.lower() == "quit": #checks for quit
        print("thanks for playing")
        break
    if user_input.isnumeric(): #checks for number
        print("This is not a letter")
    # if user_input in secret_word_list: #checks for correct letter
    #     points + 1
    #     print("yup")
    # if user_input not secret_word_list: #checks for wrong answer
    #     life - 1
    #     print("nope")
    if life == 0: #checks for lose
        print(f"You ran out of guesses. The word was {secret_word}.")
        break
    if points == 5: #checks for win
        print(f"{secret_word} is correct. You win! ")
        break
    print(" ")


##still need##
# check for letter in words
# if letter is correct: add pint and print letter












# while life > 0:
#     answer = input("guess a letter: ")
#     if answer.lower() == (): #wrong answer
#         life -= 1


# while guessed_word_correctly = False
#     guess = input("Guess a letter: ")
#     if guess == ():


# tic_tac_toe = [["X", "X", "X"],
#                ["X", "O", "X"],
#                ["X", "X", "O"]]

# print(tic_tac_toe[1][1]) # first index is "row", second index is "column", X x Y coords.







