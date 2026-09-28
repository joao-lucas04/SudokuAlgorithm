function LerSudoku(){
    let sudoku = [];
    for(let linha = 1; linha<=9; linha++){
        sudoku[linha] = [];
        for(let coluna = 1; coluna<=9; coluna++){
            let IdNum = document.getElementById(`${linha-1}${coluna-1}`)
            if(IdNum == null){
                sudoku[linha][coluna] = 0;
            } else {
                sudoku[linha][coluna] = IdNum.value
            }
        }
    }

    return sudoku;
}

function EnviaTabuleiro(){
    let tabuleiro = LerSudoku();
    console.log(tabuleiro)    
}

EnviaTabuleiro();

