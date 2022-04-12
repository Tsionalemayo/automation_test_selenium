from DataBase.Connection import Connection

class Join(Connection):
    query1=Connection().connectMySql('SELECT * FROM actor as a JOIN film_actor as f ON a.actor_id=f.actor_id WHERE film_id=530 ')

    for i in query1:
        print(i)

    query2=Connection().connectMySql('SELECT * FROM address as a JOIN city as c ON a.city_id=c.city_id')
    for f in query2:
        print(f)