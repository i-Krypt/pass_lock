class Credentials:

    '''
    class that takes in user credentials.
    '''

    credentials_list = []

    def save_credentials(self):

        '''
        saves user credentials into credentials list
        '''

        Credentials.credentials_list.append(self)

    def __init__(self, account, username, password):

        '''
        Args:
        account: New account
        username: New username
        password: New password
        '''

        self.account = account
        self.username = username
        self.password = password
