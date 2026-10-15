function LerSudoku(){
    let sudoku = [];
    for(let linha = 0; linha<=8; linha++){
        sudoku[linha] = [];
        for(let coluna = 0; coluna<=8; coluna++){
            let IdNum = document.getElementById(`${linha+1}${coluna+1}`)
            if(IdNum == null || IdNum.value === ""){
                sudoku[linha][coluna] = 0;
            } else {
                sudoku[linha][coluna] = parseInt(IdNum.value); 
            }
        }
    }

    return sudoku;
}

function EnviaTabuleiro(event){
    // Para o recarregamento padrão do formulário
    event.preventDefault();
    
    let tabuleiro = LerSudoku();
    console.log(tabuleiro) 

    fetch('/ResolveSudoku', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ tabuleiro: tabuleiro })
    })
    .then(response => response.json())
    .then(dadosRecebidos => {
        // 'dadosRecebidos' terá exatamente o que a SUA função do Python retornou
        console.log("Resposta do meu script Python:", dadosRecebidos);
    })
    .catch(erro => console.error("Erro:", erro));  
}