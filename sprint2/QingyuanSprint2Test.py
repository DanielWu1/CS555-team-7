import unittest
from QingyuanSprint2Code import PrintName, CheckMarr


class PrintNameTest(unittest.TestCase):

    def test1(self):
        AM = ["M","Alex","F","Ashe"]
        self.assertEqual(PrintName(AM), ["Alex"])

    def test2(self):
        AM = ["M","AXE","M","Alex","F","Ashe"]
        self.assertEqual(PrintName(AM), ["AXE","Alex"])


class CheckMar(unittest.TestCase):

    def test1(self):
        self.assertTrue(CheckMarr(["AXE","Alex","BOO","AXE"]), False)

    def test1(self):
        self.assertFalse(CheckMarr(["AXE","Alex","BOO"]), True)



if __name__ == "__main__":
    unittest.main()