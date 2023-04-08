import os.path

import requests as req
import re
from lxml import etree


def get_Cities():
    url = "https://tazz.ro/"
    response = req.get(url)
    with open('C:\\Users\\Alex\\Desktop\\GUI_training_UBB\\Treaba_mea\\html\\main_page.html', 'wb') as h:
        h.write(response.content)
    tree = etree.parse("C:\\Users\\Alex\\Desktop\\GUI_training_UBB\\Treaba_mea\\html\\main_page.html", etree.HTMLParser())
    root = tree.getroot()
    links = []
    for el in root.iter("li"):
        if el.getparent().getparent().attrib.get('class', None) == 'seo-cities-list':
            links.append(el.getchildren()[0].get('href'))
        # if el.attrib.get('class',None) == 'container':
        # print(el.attrib)
        # links.append(el.get('href'))
        # print(getattr(el,'href'))
        # print(type(el))
    return links


