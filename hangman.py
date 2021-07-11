import random

print('H A N G M A N')

words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
result = '-' * len(word)
attempts = 8

while attempts > 0:
    print()
    print(result)
    letter = input('Input a letter:')
    if letter in result:
        attempts -= 1
        print('No improvements')
    elif letter in word:
        index = 0
        for _ in range(word.count(letter)):
            index = word.find(letter, index)
            result = result[:index] + letter + result[index + 1:]
        if result == word:
            print('You guessed the word!')
            print('You survived!')
    else:
        attempts -= 1
        print("That letter doesn't appear in the word")
else:
    print('You lost!')
