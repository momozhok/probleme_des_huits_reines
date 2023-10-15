def solve_n_queens(n):
    # Créer un tableau vide de taille n x n pour représenter l'échiquier
    board = [[0] * n for _ in range(n)]
    # Appeler la fonction solve_backtrack avec la première reine placée sur la première colonne
    return solve_backtrack(board, 0)

def solve_backtrack(board, col):
    # Si toutes les colonnes ont été parcourues, la solution est trouvée
    if col == len(board):
        return board
    for row in range(len(board)):
        # Vérifier si la reine peut être placée dans la case (row, col)
        if is_valid(board, row, col):
            # Placer la reine dans la case (row, col)
            board[row][col] = 1
            # Récursivement placer les reines restantes sur les colonnes suivantes
            if solve_backtrack(board, col + 1) is not None:
                return board
            # Si la récursion échoue, retirer la reine de la case (row, col)
            board[row][col] = 0
    # Si aucune case valide n'a été trouvée dans la colonne actuelle, renvoyer None pour signaler l'échec de la recherche
    return None

def is_valid(board, row, col):
    # Vérifier si la reine est attaquée par une autre reine sur la même ligne
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Vérifier si la reine est attaquée par une autre reine sur la diagonale supérieure
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Vérifier si la reine est attaquée par une autre reine sur la diagonale inférieure
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Si la case est valide, renvoyer True
    return True

board = solve_n_queens(8)
for row in board:
    print(row)