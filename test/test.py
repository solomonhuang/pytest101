import unittest

class TestStringMethods(unittest.TestCase):
    '''Test class'''
    def test_upper(self):
        '''make string all upper case'''
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        '''to test string is all upper case'''
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertTrue('BAR'.isupper())

    def test_split(self):
        '''to split string'''
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

