def display_board(board):
    """Displays the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the specified player has won the game."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Checks if the Tic Tac Toe board is full."""
    for row in board:
        if ' ' in row:
            return False
    return True

def play_tic_tac_toe():
    """Plays a game of Tic Tac Toe."""
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize empty board
    current_player = 'X'
    while True:
        display_board(board)
        print(f"It's {current_player}'s turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if row not in range(3) or col not in range(3):
            print("Invalid input. Please enter a number between 0 and 2.")
            continue
        if board[row][col] != ' ':
            print("Oops! That spot is already taken. Try again.")
            continue
        board[row][col] = current_player
        if check_winner(board, current_player):
            display_board(board)
            print(f"Congratulations! {current_player} wins!")
            break
        if is_board_full(board):
            display_board(board)
            print("It's a tie! The board is full.")
            break
        current_player = 'O' if current_player == 'X' else 'X'

play_tic_tac_toe()
