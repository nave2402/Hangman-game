import random
from replit import clear
import word_list
import logos




lives = 6
random_word_list = []
chosen_word = random.choice(word_list.word_list)
random_word_list += chosen_word
new_list = []
for word in random_word_list:
    new_list += "_"
end_of_game = False
starting_image = logos.stages[6]
print(f"{logos.logo} \nWalcome to hangman game :)\n\n")
print(" ".join(new_list))
print(starting_image)
while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    clear()

    if guess in new_list:
        print(f"You have alrady guessed this letter - '{guess}'")
    # Check guessed letter
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            new_list[position] = guess
            print(" ".join(new_list))
            print(logos.stages[lives])
    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You wrong! you left {lives - 1} lives.")
        print(" ".join(new_list))
        print(logos.stages[lives - 1])

        lives -= 1

    if "_" not in new_list:
        end_of_game = True
        print("You win!!")
    elif lives == 0:
        end_of_game = True
        print(f"You lose... :( \nThe word is: {chosen_word}")
