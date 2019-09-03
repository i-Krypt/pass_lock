from user import User
from credentials import Credentials

#create a new user 
def create_user(username, password):

    '''
    Function to create a new user
    '''

    new_user = User(username, password)
    return new_user


#save user
def save_user(user):
    '''
    function to save user
    '''

    User.save_user(user)


def create_credentials(account,username,password):
    '''
    Function to create credentials
    '''

    new_credentials = Credentials(account,username,password)
    return new_credentials




#displaying credentials
def display_credentials(username):
    '''
    function that returns all the saved contacts
    '''

    return Credentials.display_credentials(username)

    #save credentials
def save_credentials(self):
    '''
    function that saves user credentials
    '''

    Credentials.save_credentials(self)

    #delete credentials
def del_credentials(credentials):
    '''
    function to delete credentials
    '''

    Credentials.delete_credentials()

#generate password
def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credentials.generate_password()
	return gen_pass


#main function.
def main():
    print(' ')
    print("Welcome to Pass Lock.")
    while True:
        print(' ')
        print("-"*60)
        print("Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit")
        short_code = input("Enter a choice: ").lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-"*60)
            print(' ')
            print("To create a new account:")
            username = input("Enter your username - ").strip()
            password = input("Enter your password - ").strip()
            # save_user()
            # print(" ")
            # print(f"New Account Created for: {username} using password: {password}")
        elif short_code == 'li':
            print("-"*60)
            print(' ')
            print("Enter account details:")
            username = input("Enter your username - ").strip()
            password = str(input("Enter your password - "))
            
            while True:
                print("-"*60)
                print("Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit")
                short_code = input('Enter a choice: ').lower().strip()
                print("-"*60)
                if short_code == 'ex':
                    print(" ")
                    print(f'logging out {username}')
                    break
                elif short_code == 'cc':
                    print(' ')
                    print("Enter your credentials:")
                    account = input("Enter account\'s name- ").strip()
                    username = input("Enter username - ").strip()
                    while True:
                        print(' ')
                        print("-"*60)
                        print("choose an option to enter password: \n ep-enter existing password \n gp-generate a password \n ex-exit")
                        psw_choice = input("Enter an option: ").lower().strip()
                        print("-"*60)
                        if psw_choice == 'ep':
                            print(" ")
                            password = input("Enter password: ").strip()
                            break
                        elif psw_choice == 'gp':
                            password = generate_password()
                            break
                        elif psw_choice == 'ex':
                            break
                        else:
                            print("Wrong option entered. Try again.")
                    save_credentials('self')
                    print(' ')
                    print(f"Credentials Created: Account: {account} - Username: {username} - Password: {password}")
                    print(' ')
                elif short_code == 'dc':
                    print(' ')
                    if display_credentials('username'):
                        print("Credentials.")
                        print(' ')
                        for credential in display_credentials('username'):
                            print(f"Account: {credential.account} - Username: {credential.username} - Password: {credential.password}")
                        print(' ')    
                    else:
                        print(' ')
                        print("Your credentials have not been saved yet")
                        print(' ')
               

        else: 
            print(' ')
            print(" Wrong details entered. Try again or Create an Account.")        
    
    else:
        print("-"*60)
        print(' ')
        print("Wrong option entered. Try again.")
            






if __name__ == '__main__':
    main()
