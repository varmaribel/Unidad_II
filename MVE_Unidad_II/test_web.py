from flask import Flask, render_template, request, redirect
from test_module import equation, equation2

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Area del Cono')


@app.route('/exec_equation', methods=['GET', 'POST'])
def execute() -> 'html':
    Ab = float(request.form['Ab'])
    Al = float(request.form['Al'])
    title = 'Este es el resultado de la ecuacion'
    result = equation(Ab, Al)
    return render_template('result.html',
                           the_title=title,
                           the_Ab=Ab,
                           the_Al=Al,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
