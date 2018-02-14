from flask import Flask, render_template, request, url_for
import data_handler
from datetime import datetime


app = Flask(__name__)


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
