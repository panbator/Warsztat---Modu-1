import random

def guess_number():
    guess = 0
    computer = random.randint(1, 100)
    guess_count = 0

    while True:
        guess_count += 1
        try:
            guess = int(input('Guess the number: '))
        except ValueError:
            print("It's not a number!")
            continue

        if guess < computer:
            print('Too small!')
        elif guess > computer:
            print('Too big!')
        else:
            print(f'You win!\nIt took you {guess_count} attempts.')
            break

guess_number()