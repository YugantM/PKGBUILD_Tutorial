import unittest
import mul

class TestClass(unittest.TestCase):
	def test_function(self):
		result = mul.mul(2,6)
		self.assertEqual(result,12)

if __name__ == "__main__":
	unittest.main()
