import random

def solve_n_queens(n):
    # Créer un tableau vide de taille n x n pour représenter l'échiquier
    board = [[0] * n for _ in range(n)]
    # Initialiser un compteur pour le nombre de tentatives
    num_attempts = 0
    # Tant que le problème n'est pas résolu
    while not is_solved(board):
        # Incrémenter le compteur de tentatives
        num_attempts += 1
        # Remettre le tableau à zéro
        board = [[0] * n for _ in range(n)]
        # Placer les reines au hasard dans chaque colonne
        for col in range(n):
            row = random.randint(0, n-1)
            board[row][col] = 1
    # Afficher le nombre de tentatives nécessaires pour résoudre le problème
    print("Nombre de tentatives :", num_attempts)
    # Renvoyer le tableau résolu
    return board

def is_solved(board):
    n = len(board)
    # Vérifier si chaque colonne contient exactement une reine
    for col in range(n):
        num_queens = 0
        for row in range(n):
            if board[row][col] == 1:
                num_queens += 1
        if num_queens != 1:
            return False
    # Vérifier si aucune paire de reines ne s'attaque mutuellement
    for row1 in range(n):
        for col1 in range(n):
            if board[row1][col1] == 1:
                for row2 in range(n):
                    for col2 in range(n):
                        if board[row2][col2] == 1 and (row1 != row2 or col1 != col2):
                            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                                return False
    # Si le tableau satisfait les conditions, renvoyer True
    return True

# Exemple d'utilisation : résoudre le problème des 8 reines
board = solve_n_queens(8)
for row in board:
    print(row)
