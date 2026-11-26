def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("\n")
    print(" | | ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print(" | | ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print(" | | ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print(" | | ")
    print("\n")

def check_win(board, player):
    winning_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]            # Diagonals
    ]
    for pattern in winning_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return all(isinstance(cell, str) for cell in board)

def play_tic_tac_toe():
    board = [str(i) for i in range(9)]  
    current_player = 'X'
    game_over = False
    moves_count = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over:
        try:
            position_str = input(f"Player {current_player}, enter a number (0-8): ")
            position = int(position_str)
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        if not (0 <= position <= 8):
            print("Invalid position. Please enter a number between 0 and 8.")
        elif isinstance(board[position], str) and board[position] in ['X', 'O']:
            print("That position is already taken! Choose another one.")
        else:
            board[position] = current_player
            moves_count += 1
            print_board(board)

            if check_win(board, current_player):
                print(f"Congratulations, Player {current_player}! You win!")
                game_over = True
            elif check_draw(board):
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

    print("Game Over.")
play_tic_tac_toe()
