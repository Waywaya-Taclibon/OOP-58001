import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Waywaya\Documents\Database1.accdb;')
    print("Connected to a Database")

    Fullname = "Waywaya B. Taclibon"
    Laboratory = 89
    Assignment = 90
    Quiz = 90
    Exam = 90
    user_id = 14

    record = connect.cursor()
    record.execute('UPDATE Databes SET Laboratory = ? WHERE id=?', (Laboratory,user_id))
    record.execute('UPDATE Databes SET Assignment = ? WHERE id=?', (Assignment, user_id))
    record.execute('UPDATE Databes SET Quiz = ? WHERE id=?', (Quiz, user_id))
    record.execute('UPDATE Databes SET Exam = ? WHERE id=?', (Exam, user_id))
    record.execute('UPDATE Databes SET Fullname = ? WHERE id=?', (Fullname, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")