class Credentials:

    '''
    class that takes in user credentials.
    '''

    credentials_list = []


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

    def save_credentials(self):

        '''
        saves user credentials into credentials list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        '''
        method deletes a saved credential from the 
        credentials_list
        '''

        Credentials.credentials_list.remove(self)


    @classmethod
    def display_credentials(cls):
        '''
        returns the credentials list
        ''' 
