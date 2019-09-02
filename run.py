from  user import User
from credentials import Credentials

#create a new user 
def create_user(username, account, password):

    '''
    Function to create a new user
    '''

    new_user = User(username, account, password)
    return new_user


#save user
def create_credentials(user):
    '''
    function to save credential
    '''

    credentials.save_credentials()