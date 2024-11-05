from lib.user import User


"""
Artist constructs with an username, email and password
"""
def test_user_constructs():
    user = User(1, "frankie5", "f@mail.co.uk", "password123")
    assert user.id == 1
    assert user.username == "frankie5"
    assert user.email == "f@mail.co.uk"
    assert user.password == "password123"

"""
We can format users to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "frankie5", "f@mail.co.uk", "password123")
    assert str(user) == "User(1, frankie5, f@mail.co.uk, password123)"


"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "frankie5", "f@mail.co.uk", "password123")
    user2 = User(1, "frankie5", "f@mail.co.uk", "password123")
    assert user1 == user2



