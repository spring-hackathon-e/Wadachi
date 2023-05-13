class User:
    def __init__(self, user_id, user_name, email, password):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.password = password

    def getUserName(self):
        return self.user_name

    def getUserEmail(self):
        return self.email

    def getUserPassword(self):
        return self.password
