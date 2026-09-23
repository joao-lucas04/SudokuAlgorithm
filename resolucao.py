sudoku = [
    [3, 0, 0,  0, 4, 9,  0, 0, 0],
    [0, 0, 0,  6, 0, 0,  5, 0, 1],
    [7, 5, 2,  0, 0, 1,  0, 0, 0],

    [0, 0, 1,  0, 0, 0,  7, 0, 0],
    [5, 0, 0,  3, 9, 6,  0, 0, 0],
    [0, 0, 8,  1, 5, 0,  0, 9, 6],

    [0, 0, 3,  0, 1, 0,  0, 6, 0],
    [0, 0, 4,  0, 0, 0,  1, 0, 0],
    [0, 0, 0,  0, 2, 8,  0, 0, 0]
]

nums = [0] * 20
numsUniverso = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
numsolucao = 0
linha = 0
coluna = 0
count = 0
countzero = 0


def LeZeroSudoku():
    global countzero, linha, coluna
    for linha in range(9):
        for coluna in range(9):
            if sudoku[linha][coluna] == 0:
                countzero += 1
    return 0


def LeQuadrante(num1, num2, num3, num4):
    global total
    for g in range(num1, num2 + 1):
        for k in range(num3, num4 + 1):
            if sudoku[g][k] != 0:
                nums[total] = sudoku[g][k]
                total += 1
    return 0


def NumErradosQuadrante(linQua, colQua):
    if linQua <= 2:
        if colQua <= 2:
            LeQuadrante(0, 2, 0, 2)
        elif colQua <= 5:
            LeQuadrante(0, 2, 3, 5)
        else:
            LeQuadrante(0, 2, 6, 8)
    elif linQua <= 5:
        if colQua <= 2:
            LeQuadrante(3, 5, 0, 2)
        elif colQua <= 5:
            LeQuadrante(3, 5, 3, 5)
        else:
            LeQuadrante(3, 5, 6, 8)
    else:
        if colQua <= 2:
            LeQuadrante(6, 8, 0, 2)
        elif colQua <= 5:
            LeQuadrante(6, 8, 3, 5)
        else:
            LeQuadrante(6, 8, 6, 8)
    return 0


def NumErradosLinha(colQua):
    global total
    if colQua <= 2:
        for num in range(3, 9):
            if sudoku[linha][num] != 0:
                nums[total] = sudoku[linha][num]
                total += 1
    elif colQua <= 5:
        for num in range(0, 3):
            if sudoku[linha][num] != 0:
                nums[total] = sudoku[linha][num]
                total += 1
        for num in range(6, 9):
            if sudoku[linha][num] != 0:
                nums[total] = sudoku[linha][num]
                total += 1
    else:
        for num in range(5, -1, -1):
            if sudoku[linha][num] != 0:
                nums[total] = sudoku[linha][num]
                total += 1
    return 0


def NumErradosColuna(linQua):
    global total
    if linQua <= 2:
        for num in range(3, 9):
            if sudoku[num][coluna] != 0:
                nums[total] = sudoku[num][coluna]
                total += 1
    elif linQua <= 5:
        for num in range(6, 9):
            if sudoku[num][coluna] != 0:
                nums[total] = sudoku[num][coluna]
                total += 1
        for num in range(0, 3):
            if sudoku[num][coluna] != 0:
                nums[total] = sudoku[num][coluna]
                total += 1
    else:
        for num in range(0, 6):
            if sudoku[num][coluna] != 0:
                nums[total] = sudoku[num][coluna]
                total += 1
    return 0


def resolveSudoku():
    global linha, coluna, total, count, countzero, numsUniverso, nums
    alterou = False
    # for duplo pra analisar a matriz
    for linha in range(9):
        for coluna in range(9):
            # caso um elemento do sudoku seja 0, armazena os numeros que
            # não podem ser nessa posição pra completar o sudoku
            if sudoku[linha][coluna] == 0:
                # Função que verifica os Nums que estão presentes no Quadrante
                NumErradosQuadrante(linha, coluna)
                # Função que verifica os Nums que estão presentes na linha do elemento analisado
                NumErradosLinha(coluna)
                # Função que verifica os Nums que estão presentes na coluna
                NumErradosColuna(linha)

                """
                A lógica será: com o vetor nums armazenando as possibilidades que não são possiveis,
                e o vetor numsUniverso sendo os numeros de 1 a 9 possiveis,
                Os numeros que serão substituidos no lugar de 0 no elemento analisado
                será a subtração dos vetores: (numsUniverso - nums) = numspos, assim o numspos será
                um novo array com os possiveis nuns daquela posição.
                """
                for posicaoUniverso in range(9):
                    for posicaoNums in range(total):
                        if numsUniverso[posicaoUniverso] == nums[posicaoNums]:
                            numsUniverso[posicaoUniverso] = 0
                            count += 1
                            break

                if count == 8:
                    countzero -= 1
                    for posicaoUniverso in range(9):  # Limitado a 9 posições para evitar estouro
                        if numsUniverso[posicaoUniverso] != 0:
                            sudoku[linha][coluna] = numsUniverso[posicaoUniverso]
                            print(f"Valor colocado no Sudoku[{linha+1}][{coluna+1}]: {sudoku[linha][coluna]}")
                            alterou = True
                            break

                count = 0

                # zera o vetor total para um novo num
                for result in range(9):
                    nums[result] = 0
                total = 0

                for posicaoUniverso in range(9):
                    numsUniverso[posicaoUniverso] = posicaoUniverso + 1

    return alterou

def NumUnicoNoQuadrante():
    global linha, coluna, total, countzero, nums
    alterou = False

    # Percorre cada um dos 9 quadrantes
    for qLinha in range(0, 9, 3):
        for qColuna in range(0, 9, 3):
            
            # Para cada número de 1 a 9
            for numero in range(1, 10):
                
                # Verifica se o número já existe neste quadrante
                ja_existe = False
                for r in range(qLinha, qLinha + 3):
                    for c in range(qColuna, qColuna + 3):
                        if sudoku[r][c] == numero:
                            ja_existe = True
                            break

                if ja_existe:
                    continue

                # Guarda quais casas do quadrante podem receber
                casas_validas = []

                for r in range(qLinha, qLinha + 3):
                    for c in range(qColuna, qColuna + 3):
                        if sudoku[r][c] == 0:
                            linha = r
                            coluna = c
                            total = 0

                            NumErradosQuadrante(linha, coluna)
                            NumErradosLinha(coluna)
                            NumErradosColuna(linha)

                            # Se o nuemro não estiver na lista de nums proibidos é valido
                            proibido = False
                            for i in range(total):
                                if nums[i] == numero:
                                    proibido = True
                                    break

                            if not proibido:
                                casas_validas.append((r, c))

                            # Limpa o vetor nums para a próxima leitura
                            for result in range(20):
                                nums[result] = 0
                            total = 0

                # Se apenas uma casa do quadrante pode receber
                if len(casas_validas) == 1:
                    r, c = casas_validas[0]
                    sudoku[r][c] = numero
                    countzero -= 1
                    print(f"Segundo Método | Valor colocado em Sudoku[{r+1}][{c+1}]: {numero}")
                    alterou = True

    return alterou


def main():
    LeZeroSudoku()

    for l in range(countzero + 1):
        resultado = resolveSudoku()

    if not resultado:
        NumUnicoNoQuadrante()

    print(countzero, end="")


if __name__ == "__main__":
    main()