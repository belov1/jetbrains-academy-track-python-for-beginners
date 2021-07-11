import random


def play():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(words)
    result = '-' * len(word)
    wrong_letters = ''
    attempts = 8

    while attempts > 0:
        print()
        print(result)
        letter = input('Input a letter:')

        if len(letter) != 1:
            print('You should input a single letter')
            continue

        if not letter.isalpha() or not letter.islower():
            print('Please enter a lowercase English letter')
            continue

        if letter in result or letter in wrong_letters:
            print("You've already guessed this letter")
            continue

        if letter in word:
            index = 0
            for _ in range(word.count(letter)):
                index = word.find(letter, index)
                result = result[:index] + letter + result[index + 1:]
            if result == word:
                print('You guessed the word!')
                print('You survived!')
                print()
                break
        else:
            wrong_letters += letter
            attempts -= 1
            print("That letter doesn't appear in the word")
    else:
        print('You lost!')
        print()


print('H A N G M A N')

while True:
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == 'play':
        play()
        break
    elif choice == 'quit':
        break
    else:
        continue
