from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from users ORDER BY id')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email"], row["password"])
            users.append(item)
        return users
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["username"], row["email"], row["password"])
    
    def create(self, user):
        if not user.username or not user.email or not user.password:
            return "You need to add a username, email, and password"
        self._connection.execute(
            'INSERT INTO users (id, username, email, password) VALUES (%s, %s, %s, %s)', 
            [user.id, user.username, user.email, user.password])
        return None
    
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [id])
        return None
    
    def update(self, user):
        self._connection.execute('UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s', [user.username, user.email, user.password, user.id])
        return None