from flask import Flask, render_template, request, url_for, redirect, session, flash
from datetime import datetime
import data_handler
import hash_handler

app = Flask(__name__)
DT_LENGTH = 19


@app.route('/incomes')
def show_incomes():
    if 'user_id' in session:
        data = data_handler.get_all_incomes(session)
        h2 = 'Incomes'
        keys = ['name', 'inc_category', 'price', 'submission_time', 'comment']
        head = {'name': 'Name',
                'inc_category': 'Income category',
                'price': 'Price',
                'submission_time': 'Date',
                'comment': 'Comment'
                }

        table = {'h2': h2,
                 'table_keys': keys,
                 'table_head': head,
                 'table_body': data
                 }
        return render_template('list_incomes.html', table=table)
    else:
        return redirect(url_for('login'))


@app.route('/expenses')
def show_expenses():
    if 'user_id' in session:
        data = data_handler.get_all_expenses(session)
        h2 = 'Expenses'
        keys = ['name', 'exp_category', 'price', 'submission_time', 'comment']
        head = {'name': 'Name',
                'exp_category': 'Expense category',
                'price': 'Price',
                'submission_time': 'Date',
                'comment': 'Comment'
                }
        table = {'h2': h2,
                 'table_keys': keys,
                 'table_head': head,
                 'table_body': data
                 }
        return render_template('list_expenses.html', table=table)
    else:
        return redirect(url_for('login'))


@app.route('/homepage')
def home():
    return render_template('registration.html')


@app.route('/')
@app.route('/account_history')
def show_account_history():
    if 'user_id' in session:
        data = data_handler.get_account_history(session)
        h2 = 'Account history'
        keys = ['name', 'category', 'price', 'submission_time', 'comment']
        head = {'name': 'Name',
                'category': 'Category',
                'price': 'Price',
                'submission_time': 'Date',
                'comment': 'Comment'
                }
        table = {'h2': h2,
                 'table_keys': keys,
                 'table_head': head,
                 'table_body': data
                 }
        balance = 0     # data_handler.get_balance(session)
        return render_template('account_history.html', table=table, balance=balance )
    else:
        return redirect('/homepage')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    alert = "passwords do not match"
    if request.method == 'POST':
        user_values = request.form.to_dict()
        hash_password = hash_handler.hash_password(user_values['password'])
        hash_verified_password = hash_handler.verify_password(user_values['verify_password'], hash_password)
        if hash_verified_password is True:
            user_values['password'] = hash_password
            data_handler.insert_registration_data(user_values)
            return redirect(url_for('home'))
        else:
            return render_template('registration.html', alert=alert)
    return render_template('registration.html')


@app.route('/add-expense', methods=['GET', 'POST'])
def add_expense():
    if 'user_id' in session:
        if request.method == 'POST':
            expense = request.form.to_dict()
            expense.update({'user_id': session['user_id'],
                            'submission_time': str(datetime.now())[:DT_LENGTH]
                            })
            data_handler.add_expense(expense)
            return redirect('/expenses')
        options = data_handler.get_exp_categories()
        return render_template('add_expense.html', options=options)
    else:
        return redirect(url_for('login'))


@app.route('/add-income', methods=['GET', 'POST'])
def add_income():
    if 'user_id' in session:
        if request.method == 'POST':
            income = request.form.to_dict()
            income.update({'user_id': session['user_id'],
                           'submission_time': str(datetime.now())[:DT_LENGTH]
                           })
            data_handler.add_income(income)
            return redirect('/incomes')
        options = data_handler.get_inc_categories()
        return render_template('add_income.html', options=options)
    else:
        return redirect(url_for('login'))


@app.route('/delete-expense/<int:expense_id>')
def delete_expense(expense_id):
    if 'user_id' in session:
        expenses = data_handler.get_all_expenses(session)
        for row in expenses:
            if expense_id == row['id']:
                data_handler.delete_expense_by_id(expense_id)

        return redirect(url_for('show_account_history'))
    else:
        return redirect(url_for('login'))


@app.route('/delete-income/<int:income_id>')
def delete_income(income_id):
    if 'user_id' in session:
        incomes = data_handler.get_all_incomes(session)
        for row in incomes:
            if income_id == row['id']:
                data_handler.delete_income_by_id(income_id)

        return redirect(url_for('show_account_history'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_data = data_handler.get_user_by_name(username)
        if user_data:
            hash_handler.verify_password(password, user_data['password'])
            session['user_id'] = user_data['id']
            session['username'] = user_data['username']
            session['name'] = user_data['name']
            return redirect('/account_history')
        else:
            flash('Invalid username or password')
            return redirect('/login')
    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    if session['user_id'] or session['username'] is not None:
        session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.secret_key = '\xf2=F\xad\xac\xa85&!UP=\xf7\x8eo,o\xbfE\xca\xc2~\xfce'
    app.run(
        port=8000,
        debug=True
    )
