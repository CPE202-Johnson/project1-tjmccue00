import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")

    def test_base15(self):
        self.assertEqual(convert(325,15),"16A")

    def test_base12(self):
        self.assertEqual(convert(335,12),"23B")

    def test_base16_2(self):
        self.assertEqual(convert(335,16),"14F")

    def test_base15_2(self):
        self.assertEqual(convert(224,15),"EE")

    def test_base14(self):
        self.assertEqual(convert(41,14),"2D")

    def test_base10(self):
        i = '6'
        j = '10'
        self.assertEqual(convert(i,j),str(i))

if __name__ == "__main__":
        unittest.main()
