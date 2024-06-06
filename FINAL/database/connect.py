import sqlite3

conn = sqlite3.connect('D:/GITHUB/Chat_App/FINAL/database/data.db')
cur = conn.cursor()


cur.execute('''
        CREATE TABLE IF NOT EXISTS login (
            username TEXT,
            password TEXT
        )
    ''')
conn.commit()
def insert(user, pwd):
    cur.execute('''INSERT INTO login(username,password) VALUES (?, ?)''', (user, pwd ))
    conn.commit()

def get():
    cur.execute('SELECT * FROM login')
    rows = cur.fetchall()
    return rows

    # Print the results
    # for row in rows:
    # print(rows[0][0])
    

def delete(key):
    cur.execute('DELETE FROM login WHERE username= ?', (key,))
    conn.commit()

def verify_credentials(username, password):
    cur.execute('SELECT * FROM login WHERE username = ? AND password = ?', (username, password))
    rows = cur.fetchall()
    return len(rows) > 0

# conn.close()

if __name__ == '__main__':
    # insert("user1",12345)
    # insert("user2",12345)
    # insert("user3",12345)
    row = get()
    # for r in row:
    #     print(r)
    








#insert('user1','12345')
#insert('user2','12345')
# get()
#insert()
#delete('user1')

# conn.close()
# name_to_delete = '{a}'

# Delete the row where the name is 'Alice'
# cur.execute('''
#     DELETE FROM login
#     WHERE username = ?
# ''', (name_to_delete,))
# conn.commit()
# get()
# Commit the changes


#cursor lets us execute SQL commands
# c.execute("""CREATE TABLE login (
#             username text,
#             password text
#             )""")
# conn.commit()


# c.execute("INSERT INTO  login VALUES('user1','join')")
# #we are inserting values into the table like employee first name, last name and pay




# def create_connection(db_file):
#     try:
#         conn=sqlite3.connect(db_file)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()


#insert

# cur.execute('''
#     INSERT INTO users (name, age, email)
#     VALUES (?, ?, ?)
# ''', ('John Doe', 30, 'john.doe@example.com'))
# conn.commit()