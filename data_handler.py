import database_common
from datetime import datetime


@database_common.connection_handler
def all_users(cursor):
    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    return users


@database_common.connection_handler
def registration(cursor, name, username, password, email):
    cursor.execute("""INSERT INTO users
                      VALUES (default, 
                              %(name)s, 
                              %(username)s, 
                              %(password_hash)s, 
                              %(email)s,
                              NULL ,
                              NULL)
                   """,
                   {'name': name,
                    'username': username,
                    'password_hash': password,
                    'email': email})


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


@database_common.connection_handler
def get_user_by_name(cursor, username):
    cursor.execute("""SELECT * FROM users
                    WHERE username = %(username)s    
                   """, {'username': username})
    return cursor.fetchone()
