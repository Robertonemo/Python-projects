import random

game_picks = ('r','p','s')
while True:
    player_choice = str(input('Select your pick (r,p,s): '))
    computer_choice = str(random.choice(game_picks))
    print(f'You chose {player_choice}\nComputer chose {computer_choice}')
    if player_choice == 'r' and computer_choice == 'p':
        print('You lose')
    elif player_choice == 'r' and computer_choice == 's':
        print('You win')
    elif player_choice == 'p' and computer_choice == 'r':
        print('You win')
    elif player_choice == 'p' and computer_choice == 's':
        print('you lose')
    elif player_choice == 's' and computer_choice == 'p':
        print('You win')
    elif player_choice == 's' and computer_choice == 'r':
        print('You lose')
    elif player_choice not in game_picks:
        print('Invalid choice. Please try again.')
    else:
        continue
    continuity = input('Do you wish to continue (y/n)').lower()
    if continuity == 'y':
        continue
    elif continuity == 'n':
        break
    else:
        print('Invalid input')
