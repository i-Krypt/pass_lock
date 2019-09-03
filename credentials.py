import random
import string

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

    
    def generate_password(size=8,char=string.ascii_uppercase+string.ascii_lowercase+string.digits):

        '''
        function that generates passwords
        '''

        gen_pass = ''.join(random.choice(char)for _ in range(size))
        return gen_pass

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

        return cls.credentials_list
