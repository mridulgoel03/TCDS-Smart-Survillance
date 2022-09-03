import sqlite3
connection = sqlite3.connect('Attendence.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
              (time,dat,body_posture,colorr,gender,age,dressing,objects,place,Description_of_incident )''')
connection.commit()
connection.close()
