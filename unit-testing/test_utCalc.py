import unittest
import utCalc

# to execute this method and check if the function is working go to terminal and type:
# python -m unittest test_utCalc.py or set it up in a: if __name__ == __main__ to run directly

# using test_ before the name of the file you want to test is the correct way of naming a test file

# pass unittest.TestCase as a parameter 
# used for checking if a function works as it should (ex.: checking answers in codewars)

class TestCalc(unittest.TestCase):

    # working with the class not the instance of the class, this will be printed 
    # at the start of the class execution 
    @classmethod
    def setUpClass(cls):
        print('SetupClass\n')

    # this will be printed 
    # at the end of the class execution
    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')

    # the setUp method will run before every method
    # its values can be used insinde other class methods
    def setUp(self):
        self.num1 = 10
        self.num2 = 5
        print('Setup')

    # tearDown method will run after every method
    def tearDown(self):
        print('tearDown')

    # the test_ naming is required so that the class knows which method to represent test
    # choose quality of the tests instead of quantity
    def test_add(self):
        
        self.assertEqual(utCalc.add(self.num1, self.num2), 15)
        self.assertEqual(utCalc.add(-1, -5), -6)
        self.assertEqual(utCalc.add(-1, 2), 1)
        print('method executed')

    def test_sub(self):
        
        self.assertEqual(utCalc.sub(self.num1, self.num2), 5)
        self.assertEqual(utCalc.sub(-1, -5), 4)
        self.assertEqual(utCalc.sub(-1, 2), -3) 
        print('method executed')

    def test_multiply(self):
        
        self.assertEqual(utCalc.multiply(self.num1, self.num2), 50)
        self.assertEqual(utCalc.multiply(-1, -5), 5)
        self.assertEqual(utCalc.multiply(-1, 2), -2)
        print('method executed')

    def test_divide(self):
        
        self.assertEqual(utCalc.divide(self.num1, self.num2), 2)
        self.assertEqual(utCalc.divide(1, 5), 1/5)
        self.assertEqual(utCalc.divide(-1, 2), -1/2)
        with self.assertRaises(ZeroDivisionError):
            utCalc.divide(10, 0)

        print('method executed')

if __name__ == '__main__':
    unittest.main()