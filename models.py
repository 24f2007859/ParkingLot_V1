import sqlite3

def create_database():
    conn = sqlite3.connect('parking.db')
    c = conn.cursor()
    table_creation_query = """
    CREATE TABLE IF NOT EXISTS USER (
        Username VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL,
        Password VARCHAR(255) NOT NULL
    );
    """
    c.execute(table_creation_query)
    conn.commit()
    print("Table is Ready")
    
#     c.execute("INSERT INTO USER VALUES ('Jitarth', '@mail.com', '12345')")
# # Display inserted data
#     print("Data Inserted in the table: ")
#     c.execute("SELECT * FROM USER")
#     for row in c.fetchall():
#         print(row)

# # Commit changes and close connection
#     conn.commit()
    conn.close()

def insertUser(username,email,password):
    con = sqlite3.connect("parking.db")
    cur = con.cursor()
    cur.execute("INSERT INTO USER (username,email,password) VALUES (?,?,?)", (username,email,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sqlite3.connect("parking.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM USER")
	users = cur.fetchall()
	con.close()
	return users