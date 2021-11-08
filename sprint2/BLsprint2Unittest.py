from BLsprint2Code import storeBirthday
from BLsprint2Code import checkParentsNotTooOld
from BLsprint2Code import checkMultipleBirths

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
        print('test first person parents')
        self.assertFalse(checkParentsNotTooOld(1940, 1960))
        print('test second person parents')
        self.assertTrue(checkParentsNotTooOld(1951, 1962))
        print('test third person parents')
        self.assertFalse(checkParentsNotTooOld(1940, 1965))
        print('test not have to much people both in same day')
        self.assertTrue(checkMultipleBirths(['San Tang', 'Yan Xiao' ]))


if __name__ =='__main__':
    unittest.main()