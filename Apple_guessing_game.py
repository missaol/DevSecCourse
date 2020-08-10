def run_apple_guessing_game(target):
   
    while True:

        guess = int(input('Guess How Many Apples I Have!'))

        if guess < target:

            print('Too Few!')

            continue
elif guess > target:
            print('Too Many!')

            continue

    else:

            print('You\'re Right!')

    return

 
run_apple_guessing_game(5)
