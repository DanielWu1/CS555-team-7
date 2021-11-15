from BLsprint3Code import storeBirthday
from BLsprint3Code import checkUniqueld
from BLsprint3Code import checkUniquename

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
        print('test id is Unique in list')
        self.assertTrue(checkUniqueld(['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9']))
        print('test name is Unique in list')
        self.assertTrue(checkUniquename(['San Tang', 'Yan Xiao', 'Qingyuan Liu', ' Feng Wu', 'Gangde Liu', 'Zhao Li', 'Xing Gao' ]))

if __name__ =='__main__':
    unittest.main()