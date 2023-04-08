from Treaba_mea.Data_extraction import extract_restaurants,data_extraction_from_tazz


def get_Dict(url):
    return extract_restaurants.get_Restaurants_Per_city(url)


def sortINC_Name(dict):
    x = list(dict.keys())
    x.sort()
    sorted_dict = {i: dict[i] for i in x}
    return sorted_dict

def sortDESC_Name(dict):
    x = list(dict.keys())
    x.sort(reverse=True)
    sorted_dict = {i:dict[i] for i in x}
    return sorted_dict

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
    x = []
    for i in l.keys():
        if l[i][0] != 'N/A' and float(l[i][0]) >= stars:
            x.append(i)
    return {i:l[i] for i in x}

def start():
    x = get_Dict("https://tazz.ro/alba-iulia/restaurante")
    print(filter_by_stars("https://tazz.ro/alba-iulia/restaurante",4))

