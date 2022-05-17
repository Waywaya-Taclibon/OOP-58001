import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Waywaya\Documents\Database1.accdb;')
    print("Connected to a Database")

    record = connect.cursor()
    record.execute('select * from Databes')
    for row in record.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error in Connection")