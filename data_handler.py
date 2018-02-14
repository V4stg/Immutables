import database_common
from datetime import datetime


@database_common.connection_handler
def all_users(cursor):
    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    return users


@database_common.connection_handler
def get_exp_categories(cursor):
    cursor.execute('''SELECT * FROM exp_categories''')
    return cursor.fetchall()


@database_common.connection_handler
def add_expense(cursor, expense):
    cursor.execute("""INSERT INTO expenses (name, exp_category_id,
                    price, submission_time, user_id, comment)
                    VALUES (%(name)s, %(exp_category_id)s,
                    %(price)s, %(submission_time)s, %(user_id)s, %(comment)s)
                    """, expense)


@database_common.connection_handler
def get_inc_categories(cursor):
    cursor.execute('''SELECT * FROM inc_categories''')
    return cursor.fetchall()


@database_common.connection_handler
def add_income(cursor, income):
    cursor.execute("""INSERT INTO incomes (name, inc_category_id,
                    price, submission_time, user_id, comment)
                    VALUES (%(name)s, %(inc_category_id)s,
                    %(price)s, %(submission_time)s, %(user_id)s, %(comment)s)
                    """, income)