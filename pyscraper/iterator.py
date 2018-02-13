import urllib2

from copy import deepcopy
from lxml import etree
from utils import get_xpath_if_exists
from selenium_utils import get_headless_driver, get_selenium_xpath_if_exists

def _gen_tree(url):
    request = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib2.urlopen(request)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    return tree

def _url_from_file(url_head, filename, url_tail='', return_var=False):
    with open(filename + '.txt', 'r') as input:
        for line in input:
            line = line.strip()
            full_url = url_head + line + url_tail

            yield (full_url, line) if return_var else full_url


def tree_from_file(url_head, filename, url_tail='', return_var=False):
    if return_var:
        for url, line in _url_from_file(url_head, filename, url_tail, return_var=return_var):
            tree = _gen_tree(url)
            yield tree, line
    else:
        for url in _url_from_file(url_head, filename, url_tail):
            tree = _gen_tree(url)
            yield tree


def url_xpath_file(url_head, filename, url_tail='', **xpath):
    for id, tree in tree_from_file(url_head, filename, url_tail):
        dict = deepcopy(xpath)
        for key, value in xpath.iteritems():
            dict[key] = get_xpath_if_exists(tree, value)
        yield id, dict


def url_tree(url_head, iterator, url_tail=''):
    for input in iterator:
        full_url = url_head + input + url_tail
        tree = _gen_tree(full_url)
        yield input, tree

def url_xpath(url_head, iterator, url_tail='', **xpath):
    for id, tree in url_tree(url_head, iterator, url_tail):
        dict = deepcopy(xpath)
        for key, value in xpath.iteritems():
            dict[key] = get_xpath_if_exists(tree, value)
        yield id, dict

def driver_iterator(url_head, iterator, url_tail=''):
    for input in iterator:
        full_url = url_head + input + url_tail
        driver = get_headless_driver()
        driver.get(input)
        return input, driver



def selenium_xpather(url_head, iterator, url_tail='', **xpath):
    for id, driver in driver_iterator(url_head, iterator, url_tail):
        dict = deepcopy(xpath)
        for key, value in xpath.iteritems():
            dict[key] = get_selenium_xpath_if_exists(driver, value)
        yield id, dict

