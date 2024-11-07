class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def is_valid(self, app):
        from flask import Flask
        from lib.database_connection import get_flask_database_connection
        from lib.user_repository import UserRepository
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)

        if not self.username:
            return False

        if not self.email or self.email.count("@") != 1:
            return False
        local_part, domain_part = self.email.split("@")
        if not local_part or not domain_part:
            return False
        if not self.email.endswith(".com"):
            return False
        
        existing_user = repository.find_by_email(self.email)
        if existing_user is not None:
            return False

        special_chars = "!@$%&"
        if (
            not self.password or
            len(self.password) < 8 or
            not any(char in special_chars for char in self.password)
        ):
            return False
        
        return True
    
    def generate_errors(self, app):
        # database connection needed to allows for email uniqueness
        from flask import Flask
        from lib.database_connection import get_flask_database_connection
        from lib.user_repository import UserRepository
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)

        special_chars = "!@$%&" # special characters for valid password 

        if not self.username:
            return "* Please add a username"

        if not self.email or self.email.count("@") != 1: # checks email is not nothing and has ony one @
            return "* Please add a valid email"
        local_part, domain_part = self.email.split("@") # checks the @ spearating two parts od the email
        if not local_part or not domain_part:
            return "* Please add a valid email"
        if not self.email.endswith(".com"): # checks valid email ending 
            return "* Please add a valid email"
        
        # checks that email does not al;ready exist in the database
        existing_user = repository.find_by_email(self.email)
        if existing_user is not None: 
            return "* This email already exists. Please use a unique email"

        if not self.password: # checks password is not nothing
            return "* Please add a valid password"
        if len(self.password) < 8: # checks password length is > 7
            return "* Your password must be at least 8 characters long"
        if not any(char in self.password for char in special_chars): # checks password coontains special chars
            return "* Your password must contain at least one of the following special character ('!', '@', '$', '%' or '&')"

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email}, {self.password})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__