import database_common


@database_common.connection_handler
def all_users(cursor):
    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    return users


@database_common.connection_handler
def get_all_incomes(cursor, session):
    cursor.execute("""
                    SELECT incomes.name, inc_category_id, price, submission_time, comment, inc_categories.name AS inc_category FROM incomes
                    INNER JOIN inc_categories ON inc_categories.id = incomes.inc_category_id
                    WHERE user_id = %(user_id)s
                    ORDER BY submission_time DESC
                    """, session)
    return cursor.fetchall()
