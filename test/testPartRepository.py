import unittest
from classes import PartRepository

class testPartRepository(unittest.TestCase):
    def testExists(self):
        pr = PartRepository.PartRepository()


if __name__ == '__main__':
    unittest.main()
