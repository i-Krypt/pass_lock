import random
from credentials import Credentials

class User:
    '''
    class that takes in user info.
    '''

    user_details = []

    def __init__(self, username, password):

        '''
        Args:
        username: New username
        password: New password

        '''

        self.username = username
        self.password = password

    def save_user(self):

        '''
        saves user details into user details.
        '''

        User.user_details.append(self)

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):

        '''
        Function to generate an 8 character password for a credential
        '''

      	gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def user_details(cls):
        '''
        returns the user details
        ''' 

        return cls.user_details