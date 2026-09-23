from main import app
from flask import render_template

#rotas
@app.route("/")
def homepae():
    return render_template("index.html")

@app.route("/ResolveSudoku")
def ResolveSudoku():
    return "Resolvi o Sudoku"