def display_board(board):
    """Print the board with row and column labels."""
    print()
    print("       0   1   2")
    for i, row in enumerate(board):
        print(f"row{i + 1}  " + " | ".join(row))
        if i < 2:
            print("      -----------")
    print()


def player_choice():
    """Player 1 picks X or O. Player 2 gets the other one."""
    player1_choice = input("Player 1, please choose X or O: ").strip().upper()

    while player1_choice not in ["X", "O"]:
        player1_choice = input("Invalid choice. Choose X or O: ").strip().upper()

    player2_choice = "O" if player1_choice == "X" else "X"
    return player1_choice, player2_choice


def player_move(player_name, symbol, board):
    """Ask the current player for a free spot. Keeps asking until it is valid."""
    while True:
        row_name = input(f"{player_name} ({symbol}), choose row1, row2, or row3: ").strip().lower()
        while row_name not in ["row1", "row2", "row3"]:
            row_name = input("Invalid choice. Choose row1, row2, or row3: ").strip().lower()

        position = input("Choose a position (0, 1, or 2): ").strip()
        while position not in ["0", "1", "2"]:
            position = input("Invalid position. Choose 0, 1, or 2: ").strip()

        row_index = int(row_name[-1]) - 1   # "row2" -> 1
        position = int(position)

        if board[row_index][position] == " ":
            return row_index, position
        print("That spot is already taken. Try again.")


def check_win(board, symbol):
    """True if `symbol` has three in a row, column or diagonal."""
    for row in board:                                   # rows
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):                                # columns
        if all(board[r][col] == symbol for r in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)):    # main diagonal
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):  # other diagonal
        return True
    return False


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def play_game():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    board = [row1, row2, row3]

    player1_choice, player2_choice = player_choice()
    players = [("Player 1", player1_choice), ("Player 2", player2_choice)]
    turn = 0   # 0 = Player 1, 1 = Player 2

    display_board(board)

    while True:
        name, symbol = players[turn]
        row_index, position = player_move(name, symbol, board)
        board[row_index][position] = symbol
        display_board(board)

        if check_win(board, symbol):
            print(f"{name} ({symbol}) wins! Congratulations!")
            break
        if board_full(board):
            print("It's a draw!")
            break

        turn = 1 - turn   # switch player


while True:
    play_game()
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing!")
        break
    print(play_game)
