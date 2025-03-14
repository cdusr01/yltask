from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
