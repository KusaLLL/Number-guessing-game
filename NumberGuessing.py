import random
print("Greetings!, We will be playing a Simple Number Guessing Game ")

Number_to_guess = random.randrange(100)

chances = 5
counter = 0

while counter < chances :
    counter =+1
    user_guess = int(input("pick a number between 1-100 :"))
    if user_guess == Number_to_guess :
        print(f'Good job The number is  {Number_to_guess} and you found it in   {counter} time')
        break

    elif counter >= chances and user_guess != Number_to_guess :
        print("Sorry the number is {Number_to_guess} pls Try Again")

    elif user_guess > Number_to_guess :
        print("Ur guess is too high!!!!")

    elif user_guess < Number_to_guess :
        print("Ur guess is too low!!!!")

    else :
        print ("Unexpected Error")
