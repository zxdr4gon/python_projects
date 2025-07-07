
num =  [ None , "1", "2", "3", "4", "5", "6", "7", "8", "9" ]


def print_board():
    print("\n")
    print(f" {num[1]} | {num[2]} | {num[3]} ")
    print("---+---+---")
    print(f" {num[4]} | {num[5]} | {num[6]} ")
    print("---+---+---")
    print(f" {num[7]} | {num[8]} | {num[9]} ")
    print("\n")


print_board()

def check_win():
    # Define all winning conditions as tuples of positions
    winning_conditions = [
        (num[1], num[2], num[3]),
        (num[4], num[5], num[6]),
        (num[7], num[8], num[9]),
        (num[1], num[4], num[7]),
        (num[2], num[5], num[8]),
        (num[3], num[6], num[9]),
        (num[1], num[5], num[9]),
        (num[3], num[5], num[7]),
    ]
    
    # Check if any condition is met
    return any(a == b == c for a, b, c in winning_conditions)


def set_position(player, position):
    # Check if the position is already filled
    if num[position] in ["X", "O"]:
        return False
    
    # Set the position with the player's mark
    num[position] = player
    return True

def check_draw():
    # Check if all positions are filled
    return all(str(f"{i}") not in (num) for i in range(1, 10))

def play_game():
    player = input("Enter your choice (X/O): ").upper()
    while player not in ["X", "O"]:
        player = input("Invalid choice.\nPlease enter X or O: ").upper()

    print_board()
    print("Enter the number where you want to place your mark.")
    print(f"Player 1: {player}\nPlayer 2: {'O' if player == 'X' else 'X'}")
    print()
    pos = input()

    # Validate input
    while pos not in [str(i) for i in range(1, 10)]:
        pos = input("Invalid number.\nPlease enter a number between 1 and 9: ")

    # Convert `pos` to integer after validation
    pos = int(pos)

    # Main game loop
    while not check_win() and not check_draw():

        if not set_position(player, pos):
            print("Position already filled. Try again.")
        
        else:
            print_board()
            if check_win():
                print(f"Player {player} wins!")
                break

            elif check_draw():
                print("It's a draw!")
                break

            player = "X" if player == "O" else "O"
        pos = input(f"Player {player}, enter your choice: ")

        while pos not in [str(i) for i in range(1, 10)]:
            pos = input("Invalid choice.\nPlease enter a number between 1 and 9: ")

        pos = int(pos)


    print("\nGame Over!")

play_game()