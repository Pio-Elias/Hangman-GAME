import random
import os
import hangman_art
import hangman_words
print(hangman_art.logo)
lives= 6
chosen_word= random.choice(hangman_words.word_list)

display= []
for letter in chosen_word:
    display += "_"

end_of_game= False

print(display)

while not end_of_game:
    
    guess= input("Guess a letter:").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter== guess:
            display[position]= letter
        
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")        
        lives-=1
        if lives == 0:
            end_of_game=True
            print("You lose!")
            print(f"The chosen word was {chosen_word}")


    print(display)
   

    if "_" not in display:
        end_of_game= True
        print("You win!")
        print(f"The chosen word was {chosen_word}")
    print(hangman_art.stages[lives])
    