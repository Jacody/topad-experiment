'''import random

def erzeuge_zufaellige_listen_anzahl(n):
    # Erstelle eine Basisliste der Zahlen
    c = list(range(1, n + 1))
    b = list(range(1, n + 1))
    a_dict = {}
    b_dict = {}
    c_dict = {}

    for i in range(1, 11):
        a_dict[f'a{i}'] = []
        b_dict[f'b{i}'] = []
        c_dict[f'c{i}'] = list(range(1, n + 1))

    #wähle zufällig aus c1 aus
    for i in range(1, 11): #gehe Spalte für Spalte durch
        zufaelliges_element = random.choice(c_dict[f'c{i}']) # Wähle ein zufälliges Element aus
        while len(a_dict[f'a{i}'])<i: #solange A weniger Elemente als i
            if zufaelliges_element not in b_dict[f'b{i}']: #wenn Bi nicht enthält
                a_dict[f'a{i}'].append(zufaelliges_element)  #Füge Ai hinzu
                c_dict[f'c{i}'].remove(zufaelliges_element)  # Entferne das ausgewählte Element aus der Liste C
                b_dict[f'b{i}'].append(zufaelliges_element)  # Füge zahl in B hinzu
            else:
                zufaelliges_element = random.choice(c_dict[f'c{i}'])



    #a_dict["a1"].append(5)


    """
    # Initialisiere eine leere Liste, um die endgültigen Listen zu speichern
    endgültige_listen = [[] for _ in range(n)]

    # Für jede Zahl in der Basisliste
    for zahl in basis:
        positionen = list(range(n))
        random.shuffle(positionen)  # Zufällige Reihenfolge der Positionen

        # Verteile jede Zahl in einer zufälligen, aber einzigartigen Position über die Listen
        for i, pos in enumerate(positionen):
            endgültige_listen[i].append((pos, zahl))

    # Sortiere jede Liste nach Positionen und entferne die Positionsinformation
    for i in range(n):
        endgültige_listen[i].sort()
        endgültige_listen[i] = [zahl for pos, zahl in endgültige_listen[i]]

    return endgültige_listen"""
    return a_dict, b_dict, c_dict

# Erzeuge die Listen
erzeugte_listen = erzeuge_zufaellige_listen_anzahl(10)

# Ausgabe der Listen
for liste in erzeugte_listen:
    print(liste)
'''
import random

def generate_magic_matrix(size):
    '''if size != 10:
        raise ValueError("Size of matrix must be 10")'''

    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    # Fill the matrix row by row
    i = 0
    while i < size:
        try:
            for j in range(size):
                nums = list(range(1,11))
                for k in range(i):
                    if matrix[k][j] in nums:
                            nums.pop(nums.index(matrix[k][j]))
                for l in range(j):
                    if matrix[i][l] in nums:
                            nums.pop(nums.index(matrix[i][l]))
                num = random.choice(nums)
                nums.pop(nums.index(num))
                matrix[i][j] = num
            i += 1
        except IndexError:
            continue
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

# Generate and print the magic matrix
#matrix = generate_magic_matrix(10)
#print_matrix(matrix)