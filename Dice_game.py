import random

Dice = [1, 2, 3, 4, 5, 6]


def ststements():
    print('1 - Would you like to play with computer.... ')
    print('2 - Would you like to play against player....')
    print('3 - Show rules : ')


def rules():
    print("========== 🎯 RULES 🎯==========")
    print("1. Turn based play")
    print("2. Press Enter to roll")
    print("3. Dice gives 1 to 6")
    print("4. Highest score wins")
    print("=============================")


def UI_1():
    print("\n==================================")
    print("        🎲 DICE MASTER 🎲         ")
    print("==================================\n")


UI_1()

while True:

    ststements()

    total_player = 0
    total_computer = 0
    total_player1 = 0
    total_player2 = 0

    print("\n------------------------------\n")

    print('Enter Your Choice : ', end=' ')
    choice = input()

    print("\n------------------------------\n")

    if choice == '1':

        name = input('Enter player name : ')

        print("\n------------------------------\n")

        try:
            rounds = int(input("Enter number of rounds: "))
        except:
            print('Invalid input, Setting rounds = 5')
            rounds = 5

        print("\n------------------------------\n")

        turn = "player"

        for i in range(rounds):

            if turn == "player":

                INPUT = input('Press enter to roll the dice : \n')

                if INPUT == "":
                    N = random.choice(Dice)
                    print("🎲 Rolling Dice...")
                    print('You got', N)
                    total_player += N
                else:
                    print('Press enter only , nothing else...')

                print("\n------------------------------\n")
                turn = 'computer'

            elif turn == "computer":

                INPUT = input('Press enter to roll the dice : \n')

                if INPUT == "":
                    N = random.choice(Dice)
                    print("🎲 Rolling Dice...")
                    print('Computer got', N)
                    total_computer += N
                else:
                    print('Press enter only , nothing else...')

                print("\n------------------------------\n")
                turn = "player"

        if total_player > total_computer:
            print('---',name, 'win !!!---')
        elif total_player == total_computer:
            print('--- Tie !!! ---')
        else:
            print('--- You lose !!! ---')

        print(f"\nYour score = {total_player}")
        print(f"Computer score = {total_computer}\n")

    elif choice == '2':

        name1 = input('Enter player 1 name : ')
        name2 = input('Enter player 2 name : ')

        print("\n------------------------------\n")

        try:
            rounds = int(input("Enter number of rounds: "))
        except:
            print('Invalid input, Setting rounds = 5')
            rounds = 5

        print("\n------------------------------\n")

        turn = "player1"

        for i in range(rounds):

            if turn == "player1":

                INPUT = input('Press enter to roll the dice : \n')

                if INPUT == "":
                    N = random.choice(Dice)
                    print("🎲 Rolling Dice...")
                    print(name1, 'got', N)
                    total_player1 += N
                else:
                    print('Press enter only , nothing else...')

                print("\n------------------------------\n")
                turn = 'player2'

            elif turn == "player2":

                INPUT = input('Press enter to roll the dice : \n')

                if INPUT == "":
                    N = random.choice(Dice)
                    print("🎲 Rolling Dice...")
                    print(name2, 'got', N)
                    total_player2 += N
                else:
                    print('Press enter only , nothing else...')

                print("\n------------------------------\n")
                turn = "player1"

        if total_player1 > total_player2:
            print('---',name1, 'win !!! ---')
        elif total_player2 > total_player1:
            print('---',name2, 'win !!! ---')
        else:
            print('---Tie !!!---')

        print(f"\n{name1} score = {total_player1}")
        print(f"{name2} score = {total_player2}\n")

    elif choice == '3':
        rules()

    else:
        print("Invalid choice, try again!")

    again = input("\nDo you want to play again ? (y/n) : ")

    print("\n------------------------------\n")

    if again.lower() == 'n':
        print('Thanks for playing !!! \n')
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("        💀 GAME OVER 💀")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        break