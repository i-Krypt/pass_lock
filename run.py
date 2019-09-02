from  user import User
from credentials import Credentials

#create a new user 
def create_user(username, password):

    '''
    Function to create a new user
    '''

    new_user = User(username, password)
    return new_user


#save user
def create_user(user):
    '''
    function to save user
    '''

    user.save_user()

#delete credentials
def del_credentials(credentials):
    '''
    function to delete credentials
    '''

    credentials.delete_credentials()


#displaying credentials
def display_credentials():
    '''
    function that returns all the saved contacts
    '''

    return Credentials.display_credentials()



#main function.

def main():
    print('Enter username')

            user_username = input()

            print(f'')