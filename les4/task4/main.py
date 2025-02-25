from flask import Flask, render_template, redirect
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = 'Миссия марс'
    return render_template('base.html', title=title)


@app.route('/list_prof/<list>')
def list_prof(list):
    data = ['инженер-исследователь', 'пилот', 'строитель',
            'экзобиолог', 'врач',
            'инженер по терраформированию', 'климатолог',
            'специалист по радиационной защите',
            'астрогеолог', 'гляциолог',
            'инженер жизнеобеспечения',
            'метеоролог', 'оператор марсохода', 'киберинженер',
            'штурман', 'пилот дронов']
    return render_template('list_prof.html', list=list, prof_list=data)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    params = {}
    params['title'] = 'Анкета'
    params['surname'] = 'Иванов'
    params['name'] = 'Иван'
    params['education'] = 'Иванович'
    params['profession'] = 'врач'
    params['sex'] = 'мужской'
    params['motivation'] = 'готов на все'
    params['ready'] = 'есть'
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
