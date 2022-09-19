from sudoku_app import app
from sudoku_app.sudoku.models import LEVEL1, verify
from flask import render_template, request
from copy import deepcopy


@app.route('/', methods=['GET', 'POST'])
@app.route('/sudoku', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answer = deepcopy(LEVEL1)
        for i in range(9):
            for j in range(9):
                if answer[i][j] == 0:
                    answer[i][j] = request.form.get(f'{i+1} {j+1}', type=int)
        if verify(answer):
            return render_template('sudoku.html', arr=LEVEL1, result="Вы выиграли!")
        else:
            return render_template('sudoku.html', arr=LEVEL1, result="Ответ не верный!")
    return render_template('sudoku.html', arr=LEVEL1, result="")

