import random

def mainGeraTabuleiro():
    tabuleiro = GeraTabu()
    print(tabuleiro)
    # return tabubuleiro

def GeraTabu():
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    indicesL= list(range(0, 4))
    indicesC = list(range(0, 9))

    tabuleiro = GerarSimetricos(tabuleiro, indicesL, indicesC)
    tabuleiro = GerarMeio(tabuleiro, indicesC)
    
    return tabuleiro

def GerarSimetricos(tabuleiro, indicesL, indicesC):
    for rodada in range(0,17):
        linhaAle = random.choice(indicesL)
        colunaAle = random.choice(indicesC)

        if(tabuleiro[linhaAle][colunaAle] == 0):
            numsPossiveis = VerificaNum(tabuleiro, linhaAle, colunaAle)
            if numsPossiveis:
                numAle = random.choice(numsPossiveis)
                tabuleiro[linhaAle][colunaAle] = numAle

                numsPossiveis = VerificaNum(tabuleiro, (8-linhaAle), colunaAle)
                if numsPossiveis:
                    numAle = random.choice(numsPossiveis)
                    tabuleiro[(8-linhaAle)][colunaAle] = numAle
                else:
                    tabuleiro[linhaAle][colunaAle] = 0
    return tabuleiro

def GerarMeio(tabuleiro, indicesC):
    Colunas = random.sample(indicesC, 3)
    linhaMeio = 4
    for colunaAle in Colunas:
        if(tabuleiro[linhaMeio][colunaAle] == 0):
            numsPossiveis = VerificaNum(tabuleiro, linhaMeio, colunaAle)
            if numsPossiveis:
                numAle = random.choice(numsPossiveis)
                tabuleiro[linhaMeio][colunaAle] = numAle

    return tabuleiro

def VerificaNum(tabuleiro, linha, coluna):
    nums = list(range(1,10))

    for num in range(1,10):
        nums = VerificaLinha(tabuleiro, linha, nums, num)
        nums = VerificaColuna(tabuleiro, coluna, nums, num)
        nums = VerificaQuadrante(tabuleiro, linha, coluna, nums, num)
    return nums

def VerificaQuadrante(tabuleiro, linha, coluna, nums, num):
    ColunaInicial = (coluna // 3) * 3
    LinhaInicial = (linha // 3) * 3
        
    for l in range(3):
        for c in range(3):
            if(tabuleiro[LinhaInicial + l][ColunaInicial + c] == num):
                try:
                    nums.remove(num)
                except ValueError:
                    pass
    return nums

def VerificaColuna(tabuleiro, coluna, nums, num):
    for i in range(9):
        if tabuleiro[i][coluna] == num:
            try:
                nums.remove(num)
            except ValueError:
                pass
    return nums

def VerificaLinha(tabuleiro, linha, nums, num):
    if num in tabuleiro[linha]:
            try:
                nums.remove(num)
            except ValueError:
                pass
    return nums

mainGeraTabuleiro()
