from lib.listing import *

class ListingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM listings")
<<<<<<< HEAD

        listings = []

        for row in rows:
            item = Listing(row['id'], row['name'], row['description'], row['price'], row['user_id'])
=======
        listings = []

        for row in rows:
            item = Listing(row["id"], row["name"], row["description"], row["price"], row["user_id"])
>>>>>>> 8924b9e435f183268c7d6efae24f8a01a78b494d
            listings.append(item)

        return listings
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM listings WHERE id = %s", [id])
        row = rows[0]
<<<<<<< HEAD
=======

>>>>>>> 8924b9e435f183268c7d6efae24f8a01a78b494d
        return Listing(row['id'], row['name'], row['description'], row['price'], row['user_id'])

    def create(self, listing):
        rows = self._connection.execute("INSERT INTO listings (name, description, price, user_id) VALUES (%s, %s, %s, %s)", [listing.name, listing.description, listing.price, listing.user_id])
<<<<<<< HEAD

        return None


    def delete(self, id):
        self._connection.execute("DELETE FROM listings WHERE id = %s", [id])

=======
        return None

    def delete(self, id):
        self._connection.execute("DELETE FROM listings WHERE id = %s", [id])
>>>>>>> 8924b9e435f183268c7d6efae24f8a01a78b494d
        return None
