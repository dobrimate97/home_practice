import random


def computer_guess(x):
    guess = 0
    a = int(input('Please enter the minimum range: '))
    b = int(input('Please enter the maximum range: '))
    while guess != x:
        guess = random.randint(a, b)
        if guess == x:
            print(f'I (the computer) have guessed the number correctly! The correct number was: {guess}')
    teszt
        print(f'My guess is {guess}, is it correct ? If it is lower than the number that you enter, write /lower/, '
              f'if higher then write /higher/')
        user_input = input('Answer: ')
        if user_input != 'higher':
            guess = random.randint(a+1, b)
        elif user_input != 'lower':
            guess = random.randint(a, b-1)
    print(f'I (the computer) have guessed the number correctly! The correct number was: {guess}')


computer_guess(10)
