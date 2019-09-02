import unittest
from user import User
from credentials import Credentials

class Tests(unittest.TestCase):

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
        self.assertEqual(self.new_user.password, '12345')

   

if __name__ == '__main__':
    unittest.main()