from flask import Flask, render_template, request, url_for
import data_handler
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('login.html')


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


if __name__ == '__main__':
    app.secret_key = '\xf2=F\xad\xac\xa85&!UP=\xf7\x8eo,o\xbfE\xca\xc2~\xfce'
    app.run(
        port=8000,
        debug=True
    )
