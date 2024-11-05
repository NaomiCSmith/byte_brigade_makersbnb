from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of Users objects reflecting the seed data.
"""
def test_get_all_users(db_connection): 
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    users = repository.all() 
    assert users == [ 
        User(1, 'Harman1', 'h@email.com', 'password123'),
        User(2, 'Naomi2', 'n@mail.co.uk', 'password123'),
        User(3, 'Doug3', 'doug@email.com', 'password123'),
        User(4, 'aaron4', 'aaron@mail.co.uk', 'password123')
    ]

def test_get_single_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find(3)
    assert user == User(3, 'Doug3', 'doug@email.com', 'password123')

def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    repository.create(User(5, "frankie5", "f@mail.co.uk", "password123"))
    result = repository.all() 
    assert result == [ 
        User(1, 'Harman1', 'h@email.com', 'password123'),
        User(2, 'Naomi2', 'n@mail.co.uk', 'password123'),
        User(3, 'Doug3', 'doug@email.com', 'password123'),
        User(4, 'aaron4', 'aaron@mail.co.uk', 'password123'),
        User(5, "frankie5", "f@mail.co.uk", "password123")
    ]

def test_create_user_with_error(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    result = repository.create(User(5, "", "f@mail.co.uk", "password123"))
    assert result == "You need to add a username, email, and password"
    assert repository.all() == [ 
        User(1, 'Harman1', 'h@email.com', 'password123'),
        User(2, 'Naomi2', 'n@mail.co.uk', 'password123'),
        User(3, 'Doug3', 'doug@email.com', 'password123'),
        User(4, 'aaron4', 'aaron@mail.co.uk', 'password123')
    ]

def test_delete_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    repository.delete(2)
    result = repository.all() 
    assert result == [ 
        User(1, 'Harman1', 'h@email.com', 'password123'),
        User(3, 'Doug3', 'doug@email.com', 'password123'),
        User(4, 'aaron4', 'aaron@mail.co.uk', 'password123')
    ]

def test_update_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    user.username = "Harharman"
    result = repository.update(user)
    assert result is None
    assert repository.all() == [
        User(1, 'Harharman', 'h@email.com', 'password123'),
        User(2, 'Naomi2', 'n@mail.co.uk', 'password123'),
        User(3, 'Doug3', 'doug@email.com', 'password123'),
        User(4, 'aaron4', 'aaron@mail.co.uk', 'password123')
    ]