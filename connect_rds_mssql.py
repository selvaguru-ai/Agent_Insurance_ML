import pymssql
import os

DB_HOST = os.getenv('DB_HOST', 'insurance.c30ekgqwow2t.us-east-2.rds.amazonaws.com')
DB_NAME = os.getenv('DB_USER', 'insurance')
DB_USER = os.getenv('DB_USER','admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'Iamwaiting$1')
DB_PORT = int(os.getenv('DB_PORT', 1433))

def connect_to_database():
    try:
        connection = pymssql.connect(server = DB_HOST, user = DB_USER, password = DB_PASSWORD, database = DB_NAME, port = DB_PORT)
        print ('Connection successful!')
        return connection
    except pymssql.DatabaseError as e:
        print ('Error connecting to the database')
        return None

def fetch_data():
    connection = connect_to_database()
    if not connection:
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ")
            results = cursor.fetchall()
            print ("Fetched Data!")
            for row in results:
                print (row)

    except pymssql.DatabaseError as e:
        print("Error Fetching Data: ", e)

    finally:
        connection.close()
        print("Connection Closed")

if __name__ == "__main__":
    fetch_data()