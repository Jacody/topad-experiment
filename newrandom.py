import random


def generate_magic_matrix(size):
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        available_nums = [set(range(1, size + 1)) for _ in range(size)]

        for j in range(size):
            # Entferne bereits verwendete Zahlen in der aktuellen Spalte und Zeile
            column_nums = set(matrix[x][j] for x in range(i))
            row_nums = set(matrix[i][:j])
            possible_nums = list(available_nums[j] - column_nums - row_nums)

            if not possible_nums:
                # Zurücksetzen und Zeile neu beginnen, wenn keine Nummern möglich sind
                matrix[i] = [0] * size
                j = -1
                continue

            num = random.choice(possible_nums)
            matrix[i][j] = num
            available_nums[j].remove(num)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))


# Beispiel der Matrixerzeugung und Ausgabe
matrix_size = 10  # Kann angepasst werden
matrix = generate_magic_matrix(matrix_size)
print_matrix(matrix)
