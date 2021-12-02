from BLsprint4Code import storeBirthday
from BLsprint4Code import checkRecentDeaths
from BLsprint4Code import checkUpcomingBirthdays

#import UserStoryCode
import unittest

class test (unittest.TestCase):

    def setUp(self):
        print ('all setup')

    def tearDown(self):
        print ('all tearDown')

    def test_sprint4(self):
        print('test store Birthday')
        self.assertTrue(storeBirthday())
        print('test List recent deaths')
        self.assertTrue(checkRecentDeaths([['02/03/2000'],['12/09/1999'],['06/13/2010'],['09/20/2013'],['02/16/2011']]))
        print('test List upcoming birthdays')
        self.assertTrue(checkUpcomingBirthdays([['03/03/2022'],['05/19/2022'],['09/19/2022'],['12/02/2022'],['4/10/2022']]))

if __name__ =='__main__':
    unittest.main()