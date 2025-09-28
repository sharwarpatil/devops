import unittest
from mathlib import is_prime   

class IsPrimeTests(unittest.TestCase):
    def test_zero(self):                 
        self.assertFalse(is_prime(0))   # 0 is not prime
    
    def test_one(self):                 
        self.assertFalse(is_prime(1))   # 1 is not prime

    def test_two(self):                 
        self.assertTrue(is_prime(2))    # 2 is prime
        
    def test_three(self):                 
        self.assertTrue(is_prime(3))    # 3 is prime

    def test_four(self):                 
        self.assertFalse(is_prime(4))   # 4 is not prime
    
    def test_five(self):                 
        self.assertTrue(is_prime(17))   # 17 is prime

    def test_six(self):                 
        self.assertTrue(is_prime(29))   # 29 is prime

    def test_seven(self):                 
        self.assertFalse(is_prime(99))  # 99 is not prime


    
if __name__ == "__main__":
    unittest.main()
