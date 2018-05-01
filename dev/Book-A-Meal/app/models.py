class User(object):
    def __init__(self, firstName=None, lastName=None, password = None):
        self._firstName = firstName
        self._lastName = lastName
        self._password = password
    
    def firstName(self):
        return self._firstName

    def lastName(self):
        return self._lastName
    
    def password(self):
        return self._password

class User_logged_in(object):
    def __init__(self, username=None, password = None):
        self._username = username
        self._password = password
    
    def username(self):
        return self._username

    def password(self):
        return self._password