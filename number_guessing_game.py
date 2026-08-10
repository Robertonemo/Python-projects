import random

#Guess The number between 1 and 100
random_number = random.randint(1,100)
count = 1
while True:
    while count <= 6:
        if count == 6:
            print(f'You are out of trials. Thank you for playing.\nThe number was {random_number}')
            break
        answer = int(input("Enter your Guess: "))
        if answer in range(101):
            if answer == random_number:
                print("Hurray you Guessed the correct number. Congratulations.")
                break
            elif answer > random_number:
                print('You guessed too high please try again')
            elif answer < random_number:
                print('You guessed too low please try again')
            else:
                print("! Invalid input !")
            count += 1
        else:
            print('Number entered is out of range try again')
    break