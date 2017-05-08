import unittest
from classes import BeautifulSoup

class TestIBeautifulSoup(unittest.TestCase):
    def testExists(self):
        bs = BeautifulSoup.iBeautifulSoup()
        soup = bs.parseHtml("<div>Happy</div>")
        self.assertEqual(soup.div.string, "Happy")

if __name__ == '__main__':
    unittest.main()
