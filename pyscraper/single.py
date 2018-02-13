import urllib2
from lxml import etree

def load_tree_from_url(url):
    response = urllib2.urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    return tree

class scraper:
    def __init__(self, url):
        self.tree = load_tree_from_url(url)

    def get_xpath_if_exists(self, xpath):
        tree = self.tree
        if 'text' in xpath:
            return tree.xpath(xpath)[0].strip() if len(tree.xpath(xpath)) > 0 else ''
        return tree.xpath(xpath)[0].text.strip() if len(tree.xpath(xpath)) > 0 else ''

