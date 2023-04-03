import lxml.etree
import requests as req
import re
from lxml import etree

def get_Cities():
    url = "https://tazz.ro/"
    response = req.get(url)
    response.raise_for_status()

    root = etree.fromstring(response.text)
    etree.tostring(root)


get_Cities()
