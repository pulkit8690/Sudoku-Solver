from flask import Flask, render_template, request
from sudoku_solver import sudoku
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/return')
def notValid():
    return render_template('return.html')

@app.route('/solution', methods=['POST','GET'])
def solution():
    sudoku_list = []
    if request.method == 'POST':

        for i in range(9):
            row_list = []
            for j in range(9):

                id = "" + str(i*9 + j)
                cell_value = request.form[id] 

                if cell_value == "":
                    row_list.append(0)
                else:
                    row_list.append(int(cell_value))

            sudoku_list.append(row_list)

        grid = sudoku(sudoku_list)
        print(grid)
        if grid.is_valid() == False:
            return render_template('return.html')
        start = time.time()
        grid.solve()
        if grid.solve() == False:
            return 'sudoku unsolveable'
        end = time.time()
        print(end-start)
        return render_template('Solution.html',solved_array = grid.return_array())
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
