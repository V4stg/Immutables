import database_common
from datetime import datetime


@database_common.connection_handler
def all_users(cursor):
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    return users


@database_common.connection_handler
def get_all_incomes(cursor, session):
    cursor.execute('''SELECT incomes.id, incomes.name, inc_category_id, price, submission_time, comment, inc_categories.name 
                      AS inc_category FROM incomes
                      INNER JOIN inc_categories 
                        ON inc_categories.id = incomes.inc_category_id
                      WHERE user_id = %(user_id)s
                      ORDER BY submission_time DESC
                    ''', session)
    return cursor.fetchall()


@database_common.connection_handler
def get_all_expenses(cursor, session):
    cursor.execute('''SELECT expenses.id, expenses.name, exp_category_id, price, submission_time, comment, exp_categories.name 
                      AS exp_category FROM expenses
                      INNER JOIN exp_categories 
                        ON exp_categories.id = expenses.exp_category_id
                      WHERE user_id = %(user_id)s
                      ORDER BY submission_time DESC
                    ''', session)
    return cursor.fetchall()


@database_common.connection_handler
def get_account_history(cursor, session):
    cursor.execute('''SELECT 'exp' AS type, expenses.id, expenses.name, -price AS price, submission_time, comment,
                        exp_categories.name AS category
                        FROM expenses
                        FULL JOIN exp_categories
                          ON exp_categories.id = expenses.exp_category_id
                          WHERE user_id = %(user_id)s
                      UNION ALL
                      SELECT 'inc' AS type, incomes.id, incomes.name, price, submission_time, comment,
                        inc_categories.name AS category
                        FROM incomes
                        FULL JOIN inc_categories
                          ON inc_categories.id = incomes.inc_category_id
                          WHERE user_id = %(user_id)s
                      ORDER BY submission_time DESC
                    ''', session)
    return cursor.fetchall()


@database_common.connection_handler
def insert_registration_data(cursor, user_data):
    cursor.execute('''INSERT INTO users (name, username, password, email, submission_time, role)
                      VALUES (%(name)s, 
                              %(username)s, 
                              %(password)s, 
                              %(email)s,
                              NULL ,
                              NULL)
                   ''', user_data)
    


@database_common.connection_handler
def get_exp_categories(cursor):
    cursor.execute('''SELECT * FROM exp_categories''')
    return cursor.fetchall()


@database_common.connection_handler
def add_expense(cursor, expense):
    cursor.execute('''INSERT INTO expenses (name, exp_category_id, price, submission_time, user_id, comment)
                      VALUES (%(name)s,
                              %(exp_category_id)s,
                              %(price)s,
                              %(submission_time)s,
                              %(user_id)s,
                              %(comment)s)
                    ''', expense)


@database_common.connection_handler
def get_inc_categories(cursor):
    cursor.execute('''SELECT * FROM inc_categories''')
    return cursor.fetchall()


@database_common.connection_handler
def add_income(cursor, income):
    cursor.execute('''INSERT INTO incomes (name, inc_category_id,
                    price, submission_time, user_id, comment)
                    VALUES (%(name)s, 
                            %(inc_category_id)s,
                            %(price)s,
                            %(submission_time)s,
                            %(user_id)s,
                            %(comment)s)
                    ''', income)


@database_common.connection_handler
def delete_expense_by_id(cursor, id):
    cursor.execute('''DELETE FROM expenses 
                      WHERE id = %(id)s  
                   ''', {'id': id})


@database_common.connection_handler
def get_user_by_name(cursor, username):
    cursor.execute('''SELECT * FROM users
                    WHERE username = %(username)s    
                   ''', {'username': username})
    return cursor.fetchone()
