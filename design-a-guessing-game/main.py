import random

correct_guess = False
random_number = random.randrange(100)
while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")
    number = int(user_input)
    try:
        if number == random_number:
            correct_guess = True
            break
        elif number < random_number:
            print("Too Low")
        else:
            print("Too High")
    except:
        print("Please enter a valid number")

print("You guessed the right number!")

