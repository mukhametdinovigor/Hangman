import random
import string
print('H A N G M A N')
option = ''
while True:
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == 'exit':
        break
    elif option != 'play':
        continue
    puzzled_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
    encoded = list('-' * len(puzzled_word))
    user_numbers = 0
    user_letters = set()
    while user_numbers < 8 and ''.join(encoded) != puzzled_word:
        print()
        print(''.join(encoded))
        user_letter = input('Input a letter: ')
        if len(user_letter) != 1:
            print('You should print a single letter')
            continue
        if user_letter not in string.ascii_lowercase:
            print('It is not an ASCII lowercase letter')
            continue
        if user_letter in puzzled_word and user_letter not in user_letters:
            for _ in range(len(puzzled_word)):
                if user_letter == puzzled_word[_]:
                    encoded[_] = user_letter
            user_letters.add(user_letter)
        elif user_letter in puzzled_word and user_letter in user_letters:
            print('You already typed this letter')
            user_letters.add(user_letter)
        elif user_letter not in puzzled_word and user_letter not in user_letters:
            print('No such letter in the word')
            user_letters.add(user_letter)
            user_numbers += 1
        elif user_letter in user_letters:
            print('You already typed this letter')
    if ''.join(encoded) == puzzled_word:
        print('You guessed the word!\nYou survived!')
    else:
        print('You are hanged!')
    print()
