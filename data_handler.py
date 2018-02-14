import database_common


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
                   {'name': name, 'username': username, 'password_hash': password, 'email': email})
