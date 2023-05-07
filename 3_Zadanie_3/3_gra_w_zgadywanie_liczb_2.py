print("Imagine a number between 0 and 1000!")
print("Press 'Enter' to continue")
input()

def imagine_number():
    min = 0
    max = 1000
    guess = int((max - min) / 2) + min
    i = 0
    replies = ['too big', 'too small', 'you win']

    while i < 10:
        print(f'{i + 1}. Is your number {guess}?')
        try:
            user_response = input('Too big, Too small, You win?: ').strip().lower()
            if user_response not in replies:
                raise ValueError("Invalid input, please type one of the answers.")
        except ValueError as e:
            print(e)
            continue

        if user_response == 'too big':
            max = guess
        elif user_response == 'too small':
            min = guess
        elif user_response == 'you win':
            print(f'Computer guessed your number in {i + 1} attempts.')
            break

        guess = int((max - min) / 2) + min
        i += 1
    else:
        print("User cheated!")

imagine_number()
