def print_board(board):
    print("\n".join(map(str, board)))

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def get_move(player):
    move = input(f"{player}, enter your move (1-9): ")
    return int(move) if 1 <= int(move) <= 9 else None

def play_game():
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"
    move_count = 0

    while move_count < 9:
        print_board(board)
        move = get_move(current_player)
        if move is None:
            print("Invalid move. Please try again.")
            continue
        x, y = divmod(move - 1, 3)
        if board[x][y] != " ":
            print("Invalid move. Please try again.")
            continue
        board[x][y] = current_player
        move_count += 1
        if check_winner(board):
            print_board(board)
            print(f"{current_player} wins!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print_board(board)
        print("It's a tie!")

play_game()