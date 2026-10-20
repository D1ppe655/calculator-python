import unittest
import logic

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(logic.add(2, 3), 5)
        
    def test_multiply(self):
        self.assertEqual(logic.multiply(4, 5), 20)
        
    def test_divide(self):
        self.assertEqual(logic.divide(10, 2), 5)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            logic.divide(10, 0)
            
    def test_percent(self):
        # 10% от 200 = 20
        self.assertEqual(logic.percent(10, 200), 20)

if __name__ == '__main__':
    unittest.main()