import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sakila"
)

# תרגיל :

#   ### יש להציג את כל הפרטים של השחקנים ששמם מתחיל באות T,A,B ##

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM actor WHERE first_name regexp "^[T,A,B]" ')

actor = mycursor.fetchall()

for a in actor:
    print(a)


###יש להציג את שמות הסרטים שהזמן צפייה שלהם הוא בין 90 ל-120  דקות

mycursor = mydb.cursor()

mycursor.execute('SELECT title,length FROM film WHERE length between 90 and 120 ')

film = mycursor.fetchall()

for f in film:
    # print(f)
    print("Movie Name:",f[0], "\nLenght:",f[1])


