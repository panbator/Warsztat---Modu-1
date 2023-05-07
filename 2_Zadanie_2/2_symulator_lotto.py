import random


def play_lotto():
    lotto_numbers = random.sample(range(1, 50), 6)
    user_numbers = []
    i = 0
    while i < 6:
        try:
            user_input = int(input(f"Enter {i + 1} number: "))
        except ValueError:
            print('Enter an integer between 1 and 49!')
            continue
        if user_input < 1 or user_input > 49:
            print("The number should be between 1 and 49, try again.")
        else:
            if user_input in user_numbers:
                print("This number has already been chosen, enter a different one.")
            else:
                user_numbers.append(user_input)
                i += 1

    count = 0
    for j in lotto_numbers:
        if j in user_numbers:
            count += 1

    print("Lotto numbers:", ", ".join(map(str, sorted(lotto_numbers))))
    print("Your numbers:", ", ".join(map(str, sorted(user_numbers))))
    print(f"Number of hits: {count}")


play_lotto()
