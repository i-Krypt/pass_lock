import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user 
    class behaviours

    '''

def setUp(self):
    '''
    runs before each test case
    ''' 
    self.new_user = User('Jeff','12345')   

def test_init(self):

    '''
    tests if objects are instatiated correctly
    '''

    self.assertEqual(self.new_user.username, 'Jeff')
    self.assertEqual(self.new_user.password, '123456')

def test_save_credentials(self):
    '''
    to test if credentials are saved successfully
    '''
    self.new_user.test_save_credentials()
    self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()