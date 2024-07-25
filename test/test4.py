'''
Functions
'''
import mysql.connector as mydb
def user():
    def serverconnection():
        global conn, cursor
        connection : bool = False
        conn = mydb.connect(
            host = "localhost",
            user = "root",
            password = "12345",
            database = "railway_management"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            connection = True
        else:
            print("Connection to server was interupted!")

    login = bool(input("Enter True/ False: "))

    # loginide = input("Enter email: ")
    loginidc = int(input("Enter contact number: "))

    if login:
        serverconnection()
        cursor.execute("SELECT * FROM users WHERE contact = {0}".format(loginidc))
        rs = cursor.fetchone()

        print(rs)
    elif not login:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        sex = input("Enter sex (M/F): ")
        email = input("Enter email: ")
        contact = int(input("Enter contact: "))

        serverconnection()
        cursor.execute("INSERT INTO users(last_name, first_name, sex, email, contact) VALUES({0}, {1}, {2}, {3}, {4})".format(last_name, first_name, sex, email, contact))
    conn.close()