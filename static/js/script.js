let IdMsgRes = document.getElementById("statusmsg");

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
        ReceberTabuleiro(dadosRecebidos);
    })
    .catch(erro => {
        console.error("Erro detalhado capturado:", erro);
        
        if (spanStatus) {
            spanStatus.innerText = "Erro ao processar o Sudoku: " + erro.message;
            spanStatus.className = "mensagem-erro";
        }
    });  
}

function ReceberTabuleiro(dados){
    let sudokuResolvido = dados.tabuleiro

    for (let linha = 0; linha <= 8; linha++) {
        for (let coluna = 0; coluna <= 8; coluna++) {
            let IdNum = document.getElementById(`${linha + 1}${coluna + 1}`);
            if(IdNum == null || IdNum.value === ""){
                if(IdNum.value === "") IdNum.classList.remove("numero-resolvido");

                // Se o input estiver vazio, preenchemos com a resposta do Python e destacamos
                if(IdNum.value === "") {
                    IdNum.value = sudokuResolvido[linha][coluna];
                    IdNum.classList.add("numero-resolvido");
                    IdMsgRes.innerText = "Sudoku resolvido!";
                    IdMsgRes.className = "mensagem-sucesso";
                }
            }
        }
    }
}

function LimparTabuleiro(){
    for (let linha = 0; linha <= 8; linha++) {
        for (let coluna = 0; coluna <= 8; coluna++) {
            let IdNum = document.getElementById(`${linha + 1}${coluna + 1}`);
            if (IdNum) {
                IdNum.classList.remove("numero-resolvido");
                IdMsgRes.innerText = "Digite o Sudoku no Tabuleiro";
                IdMsgRes.className = "mensagem-digite";
                IdNum.value = "";
            }
        }
    }  
}

document.addEventListener("DOMContentLoaded", () => {
    let formTabuleiro = document.getElementById("tabuleiroSudoku");
    let modal = document.getElementById("modalLimpar");
    let btnSim = document.getElementById("btnSim");
    let btnNao = document.getElementById("btnNao");

    if (formTabuleiro && modal) {
        // 1. Ao tentar limpar, cancela o evento nativo e ativa a modal no meio da tela
        formTabuleiro.addEventListener("reset", (event) => {
            event.preventDefault(); 
            modal.classList.add("ativa"); // Adiciona a classe que centraliza e mostra a modal
        });

        // 2. Cancelar fecha a modal
        if (btnNao) {
            btnNao.addEventListener("click", () => {
                modal.classList.remove("ativa");
            });
        }

        // 3. Confirmar limpa o tabuleiro e fecha a modal
        if (btnSim) {
            btnSim.addEventListener("click", () => {
                LimparTabuleiro();
                modal.classList.remove("ativa"); // Esconde a modal
            });
        }
    }
});
