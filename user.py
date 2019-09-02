from credentials import Credentials

class User:
    '''
    class that takes in user info.
    '''


    def __init__(self, username, password):

        '''
        Args:
        username: New username
        password: New password
        '''

        self.username = username
        self.password = password