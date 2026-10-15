# sudoku = [
#     [3, 0, 0,  0, 4, 9,  0, 0, 0],
#     [0, 0, 0,  6, 0, 0,  5, 0, 1],
#     [7, 5, 2,  0, 0, 1,  0, 0, 0],

#     [0, 0, 1,  0, 0, 0,  7, 0, 0],
#     [5, 0, 0,  3, 9, 6,  0, 0, 0],
#     [0, 0, 8,  1, 5, 0,  0, 9, 6],

#     [0, 0, 3,  0, 1, 0,  0, 6, 0],
#     [0, 0, 4,  0, 0, 0,  1, 0, 0],
#     [0, 0, 0,  0, 2, 8,  0, 0, 0]
# ]
def mainResolveSudoku(tabuleiro):
    resolveSudoku(tabuleiro)
    return tabuleiro

def resolveSudoku(sudoku):
    linha, coluna = VerificaVazio(sudoku)

    if not linha and not coluna:
         return True


    for num in range(1, 10):
        if VerificaNum(sudoku, num, linha, coluna):
            sudoku[linha][coluna] = num

            if resolveSudoku(sudoku):
                return True

            sudoku[linha][coluna] = 0

    return False

def VerificaNum(sudoku, num, linha, coluna):
    if num in sudoku[linha]:
        return False

    for i in range(9):
        if sudoku[i][coluna] == num:
            return False

    ColunaInicial = (coluna // 3) * 3
    LinhaInicial = (linha // 3) * 3

    for l in range(2):
        for c in range(2):
            if(sudoku[LinhaInicial + l][ColunaInicial + c] == num):
                return False

    return True
    
def VerificaVazio(sudoku):
    for linha in range(9):
            for coluna in range(9):
                if sudoku[linha][coluna] == 0:
                     return linha, coluna

    return None