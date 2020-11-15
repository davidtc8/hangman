#Step 3

import random
word_list = ["apple", "red", "blue"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for word in chosen_word:
    display.append('_')
print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should
#only stop once the user has guessed all the letters in the chosen_word and
#'display' has no more blanks ("_"). Then you can tell the user they've won.

#guess = input("Guess a letter: ").lower()
end_of_game = False
#Check guessed letter
while not end_of_game:
  if  '_' not in display:
    end_of_game = True
    print('You win!')
  else:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
          display[position] = letter
    print(display)

print(display)
