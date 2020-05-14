#string_test.py

import unittest # the module

#from unittest import TestCase
#clas TestStringMethods(TestCase):

#pandas.DataFrame
#unittest.TestCase

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO') #> True of False

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError): 
            #Context managers allow you to allocate and release resources precisely when you want to.
            # https://book.pythontips.com/en/latest/context_managers.html 
            s.split(2)

if __name__ == '__main__':
    unittest.main()