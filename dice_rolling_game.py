import random

#define numbers on the dice
count = 0
while True:
    dice_numbers = [1,2,3,4,5,6]
    user_input = str(input("Roll the dice (y/n): ").lower())
    if user_input == "y":
        random_pair =random.sample(dice_numbers,2)
        print(random_pair)
        count += 1
    elif user_input == 'n':
        print('Thanks For Playing')
        print(f'Number of times played is {count} time(s).')
        break
    else:
        print("!Invalid selection please try again!")
    


