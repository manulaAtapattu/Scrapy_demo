import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

# curr.execute("""CREATE TABLE quotes_db(
#             title text,
#             author text,
#             tag text
#             )""")

curr.execute("""insert INTO quotes_db values ('python is dope', 'Manula', 'python')""")

conn.commit()
conn.close()
