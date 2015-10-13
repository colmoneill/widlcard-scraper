import urllib3, sys
address = sys.argv[1]
html = urllib2.urlopen(address).read()

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(html)
from BeautifulSoup import NavigableString

def prntText(tags):
    for tag in tags:
        if tag.__class__ == NavigableString:
            print tag,
        else:
            printText(tag)

printText(soup.findAll("p"))
