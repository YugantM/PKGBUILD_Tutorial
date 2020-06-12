import unittest
import add

class TestClass(unittest.TestCase):
	def test_function(self):
		result = add.add(2,4)
		self.assertEqual(result,6)

if __name__ == "__main__":
	unittest.main()
