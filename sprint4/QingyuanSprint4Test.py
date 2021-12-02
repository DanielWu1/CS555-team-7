import unittest
from QingyuanSprint4Code import findPartialDate, rejectDate

class checkDateTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(findPartialDate(["11/13/1997", "1956", "1948"]), ["1956", "1948"])


    def test2(self):
        self.assertEqual(findPartialDate(["11/13/1997", "11/04/1956", "05/01/1948"]), [])

    def test3(self):
        self.assertEqual(findPartialDate(["11//1997", "1956", "1948"]), ["11//1997","1956", "1948"])




class checkMarriage(unittest.TestCase):

    def test1(self):
        self.assertEqual(rejectDate(["11/13/2100", "12/11/1980", "01/01/1948"]), ["11/13/2100"])

    def test2(self):
        self.assertEqual(rejectDate(["11/13/1950", "12/11/1980", "01/01/1948"]), [])

    def test3(self):
        self.assertEqual(rejectDate(["11/13/2200", "12/11/1780", "01/01/1948"]), ["11/13/2200", "12/11/1780"])


if __name__ == "__main__":
    unittest.main()