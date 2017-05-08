#!/usr/bin/env python3

"""
process-single-file.py

Usage:
  app.py <set-number>

Options:
  -h --help               Show this screen.
"""

from docopt import docopt
from classes import SetReport, HtmlGetter

if __name__ == '__main__':
    arguments = docopt(__doc__)

    print(arguments)

    htmlGetter = HtmlGetter.HtmlGetter()
    report = SetReport.SetReport(htmlGetter)
    content = report.getReportForSet(arguments['<set-number>'])
    print(content)