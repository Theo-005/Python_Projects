import random
import hangman_art
import hangman_words

print(hangman_art.logo)

lives = 6
chosen_word = random.choice(hangman_words.word_list)
placeholder = ""
length = len(chosen_word)
game_over = False
right_letters = []
guessed_letters = []

for blank in range(length):
    placeholder += "_"
print(placeholder)

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""


    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        print("You have guessed these letters: ", guessed_letters)
    else:
        guessed_letters.append(guess)
        if guess in chosen_word:       

            for letter in chosen_word:
                if letter == guess:
                    display += letter
                    right_letters.append(letter)
                elif letter in right_letters:
                    display += letter
                else:
                    display += "_"
                    
            print(display)

            if "_" not in display:
                game_over = True
                print("**************************** YOU WIN ****************************")   
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            print(hangman_art.stages[lives])
            print(f"****************************{lives} LIVES LEFT ****************************")
            if lives == 0:
                game_over = True
                print("*********************** YOU LOSE **********************")
                print(f"THE WORD WAS: {chosen_word}")


    

    