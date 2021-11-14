import unittest
from QingyuanSprint3Code import findAge, sortByAge

class checkDateTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(findAge([1997, 1956, 1948]), [24,65,73])

    def test2(self):
        self.assertEqual(findAge([1968, 1966, 1988]), [53,55,33])

    def test3(self):
        self.assertEqual(findAge([1917, 1906, 1958]), [104,115,63])




class checkMarriage(unittest.TestCase):

    def test1(self):
        self.assertTrue([21,13,47], [13,21,47])

    def test2(self):
        self.assertTrue([1,13,47], [1,21,47])

    def test3(self):
        self.assertTrue([121,13,47], [13,47,121])



if __name__ == "__main__":
    unittest.main()