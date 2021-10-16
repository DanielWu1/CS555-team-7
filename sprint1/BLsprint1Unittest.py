from sprint1Code import storeBirthday
from sprint1Code import checkDateBeforeCurrent
from sprint1Code import less150year

#import UserStoryCode
import unittest

class test (unittest.TestCase):

    def setUp(self):
        print ('all setup')

    def tearDown(self):
        print ('all tearDown')

    def test_sprint1(self):
        print('test store Birthday')
        self.assertTrue(storeBirthday())
        print('test check date before current')
        self.assertFalse(checkDateBeforeCurrent(2001))
        print('test check date before current')
        self.assertTrue(checkDateBeforeCurrent(2022))
        print('test check date before current')
        self.assertFalse(checkDateBeforeCurrent(1998))
        print('execute test_one case one')
        self.assertTrue(less150year(1998))
        print('execute test_one case two')
        self.assertFalse(less150year(1777))
        print('execute test_one case three')
        self.assertFalse(less150year(1799))



if __name__ =='__main__':
    unittest.main()