from random import choice


def createMatrix(rows, cols):
    matrix = []
    elements = "0123"
    for row in range(rows):
        matrix.append([])
        for col in range(cols):
            matrix[row].append(int(choice(elements)))
    return matrix


def printMatrix(matrix):
    print()
    for row in matrix:
        for col in row:
            print(col, end="\t")
        print()
    print()


def getOddRowsSum(matrix):
    s = 0
    for count, row in enumerate(matrix):
        if (count % 2 != 0):
            s += sum(row)
    return s


def getEvenColsSum(matrix):
    s = 0
    for row in matrix:
        for count, col in enumerate(row):
            if (count % 2 == 0):
                s += col
    return s


while (True):
    rows = input("Numero di righe della matrice: ")
    cols = input("Numero di colonne della matrice: ")

    if (rows.isdigit() and int(rows) > 0
            and cols.isdigit() and int(cols) > 0):
        rows = int(rows)
        cols = int(cols)
        break
    else:
        print("I dati devono essere numeri positivi maggiori di 0\n")

matrix = createMatrix(rows, cols)
printMatrix(matrix)

oddRows = getOddRowsSum(matrix)
print("Somma delle colonne pari:", oddRows)

evenCols = getEvenColsSum(matrix)
print("Somma delle righe dispari:", evenCols)

print("\nLa somma delle cifre riportate sulle righe dispari ", end="")
if (oddRows > evenCols):
    print("NON ", end="")
print("e' maggiore della somma delle cifre riportate sulle colonne pari")
