

#יש להגדיר Class של התחברות לבסיס נתונים ובתוכו תהיה מתודה של התחברות#

#1. יש לשלוף את כל השחקנים מטבלת שחקנים
#2. יש לשלוף את כל הסרטים מטבלת סרטים
#3.יש למנות את כמות השחקנים
#4.ישל למנות את כמות הסרטים

import mysql.connector


class Connection():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="neriya070394",
            database="sakila"
    )

    def connectMySql(self,query):
        mycursor = self.mydb.cursor()
        mycursor.execute(query)
        return mycursor.fetchall()


    def update(self,query):
        mycursor = self.mydb.cursor()
        mycursor.execute(query)

        return self.mydb.commit()
