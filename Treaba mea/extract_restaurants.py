import data_extraction_from_tazz
import time
from lxml import etree
import requests as req

def get_html(city_url):

    city = city_url.split('/')[3]
    tazz_response = req.get(f"https://tazz.ro/{city}/restaurante")
    with open(f"../html/tazz_{city}.html", 'wb') as html_file:
        html_file.write(tazz_response.content)



def get_Restaurants_Per_city(city_url):
    city = city_url.split('/')[3]
    tree = etree.parse(f'../html/tazz_{city}.html',etree.HTMLParser())
    root = tree.getroot()

def start():
    links = "https://tazz.ro/cluj-napoca/restaurante"
    #get_html(links)
    get_Restaurants_Per_city(links)

start()