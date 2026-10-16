from main import app
from flask import render_template, request, jsonify
from resolucao import mainResolveSudoku

#rotas
@app.route("/")
def homepae():
    return render_template("index.html")

@app.route("/ResolveSudoku", methods=['GET', 'POST'])
def ResolveSudoku():
    # Se o JavaScript mandou um POST com o tabuleiro:
    if request.method == 'POST':
        dados = request.get_json()
        tabuleiro = dados.get('tabuleiro')

        if not tabuleiro:
            return jsonify({'erro': 'Nenhum tabuleiro enviado'}), 400

        tabuleiro_resolvido = mainResolveSudoku(tabuleiro)

        return jsonify({
            'status': 'resolvido',
            'tabuleiro': tabuleiro_resolvido
        })

    return render_template("resolveSudoku.html")