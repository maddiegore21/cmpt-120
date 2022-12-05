def start():
    answer = "cat"
    guess_count = 0
    guess_limit = 3
    quit = "quit"

    while guess_count < guess_limit:
        guess = input('Please guess an animal: ').lower()
        guess_count += 1

        if guess == answer:
            print('Congratulations! You have guessed correctly')
            break

        elif guess == quit:
            break

        else:
            print('Your answer is incorrect, please guess again')

    return None


start()