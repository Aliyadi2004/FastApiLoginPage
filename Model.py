import mysql.connector



class Model:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost", user="root", password="", database="login"
        )
        self.myCursor = self.mydb.cursor()

    def restore(self, query):
        self.myCursor.execute(query)
        return self.myCursor.fetchall()

    def store(self, query):
        self.myCursor.execute(query)
        self.mydb.commit()
