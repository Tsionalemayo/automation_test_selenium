from DataBase.Connection import Connection
#
class Select(Connection):
    #1
    query1 = Connection().connectMySql('SELECT * FROM actor')
    for a in query1:
        print(a)

    #2
    query2 = Connection().connectMySql('SELECT * FROM film')
    for f in query2 :
        print(f)

    #3
    query3 = Connection().connectMySql('SELECT count(actor_id) FROM actor')
    print(query3)

     #4
    query4 = Connection().connectMySql('SELECT count(film_id) FROM film')
    print(query4)

