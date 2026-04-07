# random is fine for practice but better to use secrets to stop users from cheating by determining the output
import secrets

Dice = [1, 2, 3, 4, 5, 6]

def statements():
    print('\n1 - Play with computer...')
    print('2 - Play with player...')
    print('3 - Show rules...')

def show_rules():
    print("\n========== 🎯 RULES 🎯==========")
    print("1. Turn based play")
    print("2. Press Enter to roll")
    print("3. Dice gives 1 to 6")
    print("4. Highest score wins")
    print("=============================\n")
    return True

def UI_1():
    print("\n==================================")
    print("        🎲 DICE MASTER 🎲         ")
    print("==================================\n")

UI_1()

# Use descriptive function names
def player_vs_computer(player_amount=2):
    total_player = 0
    total_computer = 0

    name = input('Enter player name : ')

    if name == "":
        print('\nYou have entered wrong player name , so now the name is Player_1')
        name = 'Player_1'

    print("\n------------------------------")

    try:
        rounds = int(input("\nEnter number of rounds: \n"))
    except:
        print('\nInvalid input, Setting rounds = 5\n')
        rounds = 5

    print("------------------------------")

    turn = "player"

    # This was skipping the computer's go need a round for each player
    for i in range((rounds * player_amount)):

        if turn == "player":
            input('\n' + name + ' , enter to roll dice\n')
            N = secrets.choice(Dice)
            print(name, 'got - ', N, '🎲')
            print("\n------------------------------\n")
            total_player += N
            turn = "computer"

        else:
            input('\nComputer Enter to roll dice\n')
            N = secrets.choice(Dice)
            print('Computer got - ', N, '🎲')
            print("\n------------------------------\n")
            total_computer += N
            turn = "player"

    if total_player > total_computer:
        print(f'--- {name} wins ---🏆')
    elif total_player == total_computer:
        print('🏆--- Tie ---🏆')
    else:
        print('--- You lose ---🙁')

    print("\n------------------------------\n")

    print(name, 'score - ', total_player)
    print('Computer score - ', total_computer)

    print("\n---------------x---------------\n")
    return True

def player_vs_player(player_amount=2):
    total_player1 = 0
    total_player2 = 0

    name1 = input('Enter player 1 name : ')
    if name1 == "":
        print('\nYou have entered wrong player name , so now the name is Player_1')
        name1 = 'Player_1'

    # Removed newline and added space here to maintain consistent UI
    name2 = input('\nEnter player 2 name : ')
    if name2 == "":
        print('\nYou have entered wrong player name , so now the name is Player_2')
        name2 = 'Player_2'

    print("------------------------------\n")

    try:
        rounds = int(input("Enter number of rounds: \n"))
    except:
        print('Invalid input, Setting rounds = 5\n')
        rounds = 5

    print("------------------------------\n")

    turn = "player1"

    # Need round for each player
    for i in range((rounds * player_amount)):

        if turn == "player1":
            input('\n' + name1 + ' , enter to roll dice\n')
            N = secrets.choice(Dice)
            print(name1, 'got - ', N, '🎲')
            print("\n------------------------------\n")
            total_player1 += N
            turn = "player2"

        else:
            input('\n' + name2 + ' , enter to roll dice\n')
            N = secrets.choice(Dice)
            print(name2, 'got - ', N, '🎲')
            print("\n------------------------------\n")
            total_player2 += N
            turn = "player1"

    # How could this be updated to be better practice? 
    if total_player1 > total_player2:
        print(f'--- {name1} wins ---🏆')
    elif total_player2 > total_player1:
        print(f'--- {name2} wins ---🏆')
    else:
        print('🏆--- Tie ---🏆')

    print("\n------------------------------\n")

    print(name1, 'score - ', total_player1)
    print(name2, 'score - ', total_player2)

    return True

def invalid_choice():
    print("Invalid choice!")
    return True

def start_game():
    while True:

        statements()

        print("\n------------------------------\n")

        choice = input('Enter Your Choice : ')

        print("\n------------------------------\n")

        # Best practice to use match instead of if, elif, else
        match choice:
            case "1":
                player_vs_computer()
            case "2":
                player_vs_player()
            case "3":
                show_rules() 
            # This is the else case you were using to validate inputs     
            case _: 
                invalid_choice()  

        again = input("\nYou want to play again? (y/n): ")

        if again.lower() == 'n':
            print('Thanks for playing !!! \n')
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("        💀 GAME OVER 💀")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            break

# Use this to ensure modularity 
if __name__ == "__main__":
    start_game()
