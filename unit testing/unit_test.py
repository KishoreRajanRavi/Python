import  unittest
from tkinter.font import names

from cal import  add,sub

class test_cal(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,2),5)
    def test_sub(self):
        self.assertEqual(sub(5,2),3)

if __name__== "__main__":
 unittest.main()