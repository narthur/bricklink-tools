from bs4 import BeautifulSoup

class SetReport():
    def __init__(self, HtmlGetter):
        self.htmlGetter = HtmlGetter

    def getReportForSet(self, setNumber):
        html = self.htmlGetter.getHtml("https://www.bricklink.com/catalogPG.asp?S="+setNumber)
        if html:
            soup = BeautifulSoup(html,'html.parser')
            return next(td.next_sibling.b.text for td in soup.find_all("td") if td.text.startswith('Avg Price'))