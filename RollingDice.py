import random

game_on = True


while game_on == True:
    dice_ = input("Would you like to roll the die? Yes or No?")
    if dice_ == "Yes":
        your_num = random.randint(1, 6)
        print(str(your_num))
    elif dice_ == "No":
        print("Okay, goodbye.")
        quit()
    else:
        dice_ = input("Would you like to roll the die? Yes or No?")



