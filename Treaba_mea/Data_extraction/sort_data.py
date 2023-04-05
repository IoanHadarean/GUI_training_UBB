import extract_restaurants
import data_extraction_from_tazz


def get_Dict(url):
    return extract_restaurants.get_Restaurants_Per_city(url)


def sortINC_Name(dict):
    names = list(dict.keys())
    names.sort()
    return names


def sortDESC_Name(dict):
    names = list(dict.keys())
    names.sort(reverse=True)
    return names

def sortINC_City():
    x = data_extraction_from_tazz.get_Cities()
    x.sort(key=lambda a: a.split('/')[3])
    return x

def sortDESC_City():
    x = data_extraction_from_tazz.get_Cities()
    x.sort(reverse=True,key=lambda a:a.split('/')[3])
    return x

def filter_by_stars(city_url,stars):
    l = extract_restaurants.get_Restaurants_Per_city(city_url)
    print(l)
    x = []
    for i in l.keys():
        if l[i][0] != 'Rating not found' and float(l[i][0]) >= stars:
            x.append(i)
    return x

def start():
    for i in data_extraction_from_tazz.get_Cities():
        print(filter_by_stars(i,4.8))

start()
