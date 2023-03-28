import os
from lxml import etree


class ExtractDataFromHtmlPage:

    def __init__(self):
        self.html_file = os.path.realpath("tazz.html")
        self.parser = etree.HTMLParser()
        self.cluj_restaurants = []

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
                    self.cluj_restaurants.append(element_text)
        # 2nd approach -> use Xpaths
        cluj_restaurants = [element.text for element in root.findall('.//h3[@class="store-name"]')]
        assert sorted(cluj_restaurants) == sorted(self.cluj_restaurants)
        print(sorted(cluj_restaurants))
        print(cluj_restaurants)


extractDataObj = ExtractDataFromHtmlPage()
extractDataObj.extract_tazz_restaurants()
