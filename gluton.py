def solve_n_queens(n):
    # Créer un tableau vide de taille n x n pour représenter l'échiquier
    board = [[0] * n for _ in range(n)]
    # Placer la première reine dans la première colonne
    col = 0
    row = 0
    while col < n:
        # Chercher une case valide pour la reine dans la colonne courante
        found = False
        for i in range(row, n):
            if is_valid(board, i, col):
                found = True
                row = i
                break
        # Si une case valide a été trouvée, placer la reine dans la case correspondante
        if found:
            board[row][col] = 1
            # Passer à la colonne suivante
            col += 1
            row = 0
        else:
            # Si aucune case valide n'a été trouvée dans la colonne courante, revenir à la colonne précédente
            col -= 1
            if col >= 0:
                # Trouver la rangée de la reine dans la colonne précédente
                row = 0
                while row < n and board[row][col] != 1:
                    row += 1
                # Retirer la reine de la case correspondante
                board[row][col] = 0
                # Passer à la prochaine rangée dans la colonne précédente
                row += 1
    return board

def is_valid(board, row, col):
    # Vérifier si la reine est attaquée par une autre reine sur la même ligne
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Vérifier si la reine est attaquée par une autre reine sur la diagonale supérieure
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Vérifier si la reine est attaquée par une autre reine sur la diagonale inférieure
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    # Si la case est valide, renvoyer True
    return True

board = solve_n_queens(8)
for row in board:
    print(row)