from flask import Flask, render_template, request, url_for, redirect, session
import data_handler, hash_handler
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('home.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    alert = "passwords do not match"
    if request.method == 'POST':
        name = request.form['name']
        user_name = request.form['username']
        password = request.form['password']
        verified_password = request.form['verify_password']
        email = request.form['email']

        hash_password = hash_handler.hash_password(password)
        hash_verified_password = hash_handler.verify_password(verified_password, hash_password)

        if hash_verified_password is True:
            data_handler.registration(name, user_name, hash_password, email)
            return render_template('login.html')
        else:
            return render_template('registration.html', alert=alert)
    return render_template('registration.html')


@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        expense = request.form.to_dict()
        expense.update({'user_id': session['user_id'], 'submission_time': datetime.now()})
        data_handler.add_expense(expense)
        return redirect('/')
    options = data_handler.get_exp_categories()
    return render_template('add_expense.html', options=options)


@app.route('/add-income', methods=['GET', 'POST'])
def add_income():
    if request.method == 'POST':
        income = request.form.to_dict()
        income.update({'user_id': session['user_id'], 'submission_time': datetime.now()})
        data_handler.add_income(income)
        return redirect('/')
    options = data_handler.get_inc_categories()
    return render_template('add_income.html', options=options)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_data = data_handler.get_user_by_name(username)
        if user_data is None:
            return redirect('/login')

        if hash_handler.verify_password(password, user_data['password']):
            session['user_id'] = user_data['id']
            session['username'] = user_data['username']
            session['name'] = user_data['name']
            return redirect('/homepage')

        else:
            return render_template('login.html', alert='invalid password')

    else:
        return render_template('login.html')





if __name__ == '__main__':
    app.secret_key = '\xf2=F\xad\xac\xa85&!UP=\xf7\x8eo,o\xbfE\xca\xc2~\xfce'
    app.run(
        port=8000,
        debug=True
    )
