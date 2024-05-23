import numpy as np
import random

# Initialize the game board
def create_empty_board():
    return np.zeros((3, 3), dtype=int)

# Find all empty cells on the board
def get_empty_cells(board):
    empty_cells = list(zip(*np.where(board == 0)))
    return empty_cells

# Check if a player has won the game
def has_winner(board, player):
    for row in board:
        if np.all(row == player):
            return True

    for col in board.T:
        if np.all(col == player):
            return True

    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False

# Evaluate the game state to determine the winner
def get_winner(board):
    for player in [1, 2]:
        if has_winner(board, player):
            return player

    if not get_empty_cells(board):
        return -1  # Tie

    return 0  # Game continues

# Function to make a move at the specified position
def make_move(board, position, player):
    if board[position] == 0:
        board[position] = player
        return board
    else:
        raise ValueError("The position is already occupied")

# Function to get the user move
def get_user_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if (row, col) in get_empty_cells(board):
                return (row, col)
            else:
                print("The position is already occupied or invalid. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

# Function for computer to make a random move
def make_random_move(board, player):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = player
        print(f"Computer places at position {move}")
    return board

# Main function to run the Tic Tac Toe game
def play_tictactoe():
    board = create_empty_board()
    print("Initial Board:")
    print(board)

    current_winner = 0
    move_counter = 1

    while current_winner == 0:
        # Player 1 (Human) move
        print("\nYour turn (Player x)")
        user_move = get_user_move(board)
        board = make_move(board, user_move, 1)
        print(f"\nBoard after move {move_counter} (Player x):")
        print(board)
        move_counter += 1
        current_winner = get_winner(board)
        if current_winner != 0:
            break

        # Player 2 (Computer) move
        print("\nComputer's turn (Player y)")
        board = make_random_move(board, 2)
        print(f"\nBoard after move {move_counter} (Player y):")
        print(board)
        move_counter += 1
        current_winner = get_winner(board)

    if current_winner == -1:
        print("\nThe game is a tie!")
    else:
        print(f"\nThe winner is Player {current_winner}!")
    return current_winner

# Run the game
play_tictactoe()
