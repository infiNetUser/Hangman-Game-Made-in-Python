import random

def generate_word():
    words = ['Happy', 'Dog', 'Book', 'Tree', 'Laugh', 'Cat', 'Ball', 'Run', 'Hat', 'Sun', 'Big', 'Red', 'House', 'Fish', 'Python', 'Car', 'Smile', 'Door', 'Hat', 'Moon', 'Walk', 'Blue', 'Milk', 'Bed', 'Bird', 'Flower', 'Sing', 'Box', 'Grass', 'Cup', 'Orange', 'Chair', 'Apple', 'Snow', 'Bread', 'Frog', 'Beach', 'Music', 'Key', 'Duck', 'Juice', 'Ship', 'Hat', 'Bike', 'Game', 'Fan', 'Horse', 'Pen', 'Train', 'Phone']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

word = generate_word().lower()
guessed_letters = set()
lives = 4

print("Welcome to Hangman!")
print("You have 4 lives, if you get all of them wrong you lose! If you get all of them right, you win!")
print(display_word(word, guessed_letters))

while lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You've already guessed that letter. Try again!")
        continue
    guessed_letters.add(guess)
    if guess in word:
        print("Correct!")
        if all(letter in guessed_letters for letter in word):
            print("You win!")
            break
    else:
        lives -= 1
        print("Incorrect!")
        if lives == 0:
            print("You lose! The word was:", word)
            break
    print(f"{lives}/4 lives")
    print(display_word(word, guessed_letters))
