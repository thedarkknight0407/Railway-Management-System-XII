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

        return connection   
    if serverconnection():
        login = int(input("Enter 1 for login, 2 for sign-up: "))


        # loginide = input("Enter email: ")

        if login == 1:
            loginidc = int(input("Enter contact number: "))
            if len(str(loginidc)) == 10:
                cursor.execute("SELECT * FROM users WHERE contact = {0}".format(loginidc))
                rs = cursor.fetchone()
            else:
                print("Contact number is invalid!")

            print(rs)

        elif login == 2:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            sex = input("Enter sex (M/F): ")
            email = input("Enter email: ")
            contact = int(input("Enter contact: "))

            if len(str(contact)) == 10:
                user_data = (last_name, first_name, sex, email, contact)
                query = f"insert into users(last_name, first_name, sex, email, contact) values{user_data}"
                cursor.execute(query)
                conn.commit()
            
            else:
                print("Contact number is invalid!")
        conn.close()