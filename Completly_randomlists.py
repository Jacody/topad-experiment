import random

def generate_magic_matrix(n):
    matrix = []
    for _ in range(n):
        # Erstelle eine Permutation der Zahlen 1 bis n für jede Zeile
        row = random.sample(range(1, n + 1), n)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


# Generiere und drucke die Matrix
#matrix = generate_magic_matrix(10)
#print_matrix(matrix)