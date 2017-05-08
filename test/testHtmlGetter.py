import unittest
from classes import HtmlGetter

class MyTestCase(unittest.TestCase):
    def testExists(self):
        hg = HtmlGetter.HtmlGetter()
        hg.getHtml( "http://google.com/" )

if __name__ == '__main__':
    unittest.main()
