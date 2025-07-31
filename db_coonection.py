import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass1234",
    database="training"
)

if mydb.is_connected():
    print("The connection has been established")
    print("-----------------------------------")

    c = mydb.cursor()
    query = "SELECT * FROM student"
    c.execute(query)
    rows = c.fetchall()

    for i in rows:
        print("ID: {}".format(i[0]))
        print("Name: {}".format(i[1]))
        print("Age: {}".format(i[2]))
        print("Course: {}".format(i[3]))
        print("-----------------------------------")

    c.close()
    mydb.close()
else:
    print("Failed to connect to the database.")