from  user import User
from credentials import Credentials


def create_user(username, account, password):

    '''
    Function to create a new user
    '''

    new_user = User(username, account, password)
    return new_user