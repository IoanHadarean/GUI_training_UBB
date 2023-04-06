from Treaba_mea.Data_extraction import data_extraction_from_tazz
import time
from lxml import etree
import requests as req


def get_html(city_url):
    city = city_url.split('/')[3]
    tazz_response = req.get(f"https://tazz.ro/{city}/restaurante")
    with open(f"../Treaba_mea/html/tazz_{city}.html", 'wb') as html_file:
        html_file.write(tazz_response.content)


def get_Restaurants_Per_city(city_url):
    city = city_url.split('/')[3]
    tree = etree.parse(f'html/tazz_{city}.html', etree.HTMLParser())
    root = tree.getroot()
    dict = {}
    for el in root.iter("div"):
        t = None
        l = "Rating not found"
        deliv = None
        if el.attrib.get('class', None) == "store-info":
            if len(el.getchildren()) >= 2:
                for ct, i in enumerate(el.getchildren()[1].itertext()):
                    if ct == 1:
                        l = i.strip()
                # print(dir(el.getchildren()[1]))
                # print(el.getchildren()[0].text, l)
            t = el.getchildren()[0].text
            x = el.getnext().getchildren()[0]
            for ct, i in enumerate(x.itertext()):
                if ct == 2:
                    deliv = i.strip()
        if t is not None and deliv is not None:
            dict[t] = [l, deliv]
    return dict


def start():
    links = data_extraction_from_tazz.get_Cities()
    # print(links)
    #  for i in links:
    #      get_html(i)
    #      get_Restaurants_Per_city(i)

    for rest in links:
        print(get_Restaurants_Per_city(rest))
        city = rest.split('/')[3]
        print(f"DONE WITH {city.upper()}")
        time.sleep(2)
    #print(get_Restaurants_Per_city("https://tazz.ro/petrosani/restaurante"))

