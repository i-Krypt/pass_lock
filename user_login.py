import time

#profile
Username = ('Jeff')
Password = ('1234')

#user input
inputUser = ('Username: ')
inputPass = ('Password: ')

# user input condition

if inputUser == Username:
    print('')

else:
     print('Invalid Username or Password')
     time.sleep(5)
     quit()

#password input condition
if inputPass == Password:
        print('Log in successful')
        time.sleep(5)

else:
        print('Invalid username or password')
        time.sleep(5)  
        quit()      