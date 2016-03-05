import unittest
from a2.Python.Var2.Pawned import Pawned

class TestPawned(unittest.TestCase):

    def test_str(self):
        p = Pawned(None)
        print(p.str())
        # self.assertEqual('foo'.upper(), 'FOO')


    if __name__ == '__main__':
        unittest.main()