import random
import hangman_words
import hangman_art
# word_list = ["ardvark", "baboon", "camel"]


print(hangman_art.logo)
word = random.choice(hangman_words.word_list)
n = len(word)
# print(word)
display = []
for i in range(n):
    display.append("_")

print(f"The word is: {display}\t\t\t",hangman_art.stages[6])

lives = 6
currlife = hangman_art.stages[lives]
def get_curr_life():
    return hangman_art.stages[lives]

while lives>0:
    guess = input("Guess a letter!\n").lower()
    count=0
    if guess == word:
        print("You WIN!")
    for i in range(n):
        if (guess == word[i]):
            count+=1
            display[i] = guess
    if count>0:
        print(display)
        x = ''.join(display)
        if x == word:
            print("You guessed the word! You Win!")
            break

    else:
        lives-=1
        print(display)
        print(f"Lives remaining: {lives}")
        print(get_curr_life())
if(lives==0):
    print("Games Over! YOU LOSE")


