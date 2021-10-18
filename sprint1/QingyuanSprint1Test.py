import unittest
from QingyuanSprint1Code import checkDate, CheckMarriage


class checkDateTest(unittest.TestCase):

    def test1(self):
        self.assertFalse(checkDate(2018, 1999), False)

    def test2(self):
        self.assertTrue(checkDate(1950, 1990), False)

    def test3(self):
        self.assertFalse(checkDate(1990, 1970), False)

    def test4(self):
        self.assertFalse(checkDate(1975, 1970), False)

class checkMarriage(unittest.TestCase):

    def test1(self):
        self.assertTrue(CheckMarriage(1980,1983,2000), True)

    def test2(self):
        self.assertTrue(CheckMarriage(1950,1953, 1980), True)

    def test3(self):
        self.assertFalse(CheckMarriage(1960,1963, 1970), False)

    def test4(self):
        self.assertFalse(CheckMarriage(1960,1960, 1974), False)

if __name__ == "__main__":
    unittest.main()