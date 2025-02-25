from flask import Flask, render_template, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return render_template('success.html', title='Успешная авторизация')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
