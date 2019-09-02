from credentials import Credentials

class User:
    '''
    class that takes in user info.
    '''


    def __init__(self, username, account, password):

        '''
        Args:
        username: New username
        account: New account
        password: New password

        '''

        self.username = username
        self.password = password