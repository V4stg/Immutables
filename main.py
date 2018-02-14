from flask import Flask, render_template, request, url_for
import data_handler

app = Flask(__name__)


@app.route('/incomes')
def show_incomes():
    data = data_handler.get_all_incomes(session)
    keys = ['name', 'inc_category', 'price', 'submission_time', 'comment']
    head = {'name': 'Name', 'inc_category': 'Income category', 'price': 'Price', 'submission_time': 'Date', 'comment': 'Comment'}
    table = {'keys': keys, 'head': head, 'body': data}
    return render_template('list.html', table=table)
