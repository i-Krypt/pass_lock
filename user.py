import random
import string
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



    @classmethod
    def user_details(cls):
        '''
        returns the user details
        ''' 

        return cls.user_details