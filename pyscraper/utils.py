import json
import urllib2
from lxml import etree

import requests


# def file_data_loader(filename, )

def get_xpath_if_exists(tree, xpath):
    if len(tree.xpath(xpath)) < 1:
        return ''
    text = tree.xpath(xpath)[0] if 'text' in xpath else tree.xpath(xpath)[0].text
    return text.strip() if text else ''


