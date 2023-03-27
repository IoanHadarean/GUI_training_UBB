import os
from lxml import etree


class ExtractDataFromHtmlPage:

    def __init__(self):
        self.html_file = os.path.realpath("tazz.html")
        self.parser = etree.HTMLParser()

    def extract_tazz_restaurants(self):
        tree = etree.parse(self.html_file, self.parser)
        root = tree.getroot()
        html_data = etree.tostring(tree.getroot(), pretty_print=True, method="html")
        # 1st approach -> iterate through entire tree
        for element in root.findall(".//"):
            if element.tail is not None:
                element_tail = element.tail
            if element.tag == "h3":
                class_attribute = element.attrib.get('class', None)
                if class_attribute is not None and class_attribute == 'store-name':
                    element_text = element.text


extractDataObj = ExtractDataFromHtmlPage()
extractDataObj.extract_tazz_restaurants()
