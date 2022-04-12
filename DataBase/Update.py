from DataBase.Connection import Connection

class Update(Connection):
    query1=Connection().update('UPDATE actor SET first_name="Tsiona" WHERE first_name="TS" ')

    x=Connection().connectMySql('SELECT * FROM actor')
    print(x)
