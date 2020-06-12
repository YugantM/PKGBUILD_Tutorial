import unittest
import calc

class TestClass(unittest.TestCase):
	def test_function(self):
		result = calc.calc(0,2,4)
		self.assertEqual(result,6)
		self.assertEqual(calc.calc(1,4,7),28)

if __name__ == "__main__":
	unittest.main()

