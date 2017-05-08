from bs4 import BeautifulSoup

class iBeautifulSoup():
    def parseHtml(self, html):
        return BeautifulSoup(html, 'html.parser')