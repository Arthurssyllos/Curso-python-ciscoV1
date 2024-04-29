from random import randrange

def print_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def check_win(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def user_move(board):
    while True:
        try:
            move = int(input("Digite seu movimento: "))
            row = (move - 1) // 3
            col = (move - 1) % 3
            if 1 <= move <= 9 and board[row][col] == str(move):
                board[row][col] = 'O'
                break
            else:
                print("Movimento inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def computer_move(board):
    while True:
        move = randrange(9) + 1
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] == str(move):
            board[row][col] = 'X'
            break

def tic_tac_toe():
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    print_board(board)

    for _ in range(4):  # Max 4 moves for tic-tac-toe
        user_move(board)
        print_board(board)
        winner = check_win(board)
        if winner:
            if winner == 'O':
                print("Parabéns! Você ganhou!")
            else:
                print("O computador ganhou!")
            return
        computer_move(board)
        print_board(board)
        winner = check_win(board)
        if winner:
            if winner == 'X':
                print("O computador ganhou!")
            else:
                print("Parabéns! Você ganhou!")
            return

    print("Empate!")

if __name__ == "__main__":
    tic_tac_toe()
