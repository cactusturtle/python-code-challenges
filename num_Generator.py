import random
number_of_guesses = 0
get_input = input("Give me a number: ")
use_input = int(get_input)

my_number = random.randint(1, use_input)

get_guess = input("Guess a number between 1 and " + str(use_input))
use_guess = int(get_guess)
number_of_guesses += 1

while use_guess != my_number:
    if use_guess > my_number:
        new_guess = input("it's lower than " + str(use_guess) + "\n Try again: ")
        use_guess = int(new_guess)
        number_of_guesses +=1
    if use_guess < my_number:
        new_guess = input("It's higher than " + str(use_guess) + "\n Try again: ")
        use_guess = int(new_guess)
        number_of_guesses += 1

if use_guess == my_number:
    print("You got it right! It is " + str(my_number) + " And it only took you " + str(number_of_guesses) + " tries!")