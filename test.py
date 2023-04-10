import requests
from bs4 import BeautifulSoup
import re

#codu scrie intrun fisier text pentru fiecare oras restaurantele cu detaliile lor



url = 'https://tazz.ro/'
response = requests.get(url)
soup1 = BeautifulSoup(response.content, 'html.parser')

#Gasim lista de orase care se afla intr-un div cu clasa respectiva
elements = soup1.find_all('a', {'class': 'city-card address-check'})

#lista orase
cities = []

#Flitram orasele din link care e de forma https://tazz.ro/galati/oras
#filtram numele si luam al 16 caracter locu unde se termina prima parte pana la
# la /  unde se termina practic dupa il bagam in lista de orase
for element in elements:
    href = element.get('href')
    start = 16
    end = href.index('/', start)
    cityName = href[start:end]
    cities.append(cityName)

#am bagat asta sa verific daca le-a luat bine
#for city in cities:
#    print(city)

#oke partea a doua facem request sa obtinem lista de restaurante pentru fiecare oras



file = open("ListaFull.txt", "w", encoding='utf-8')

#ia fiecare oras in parte de pe pagina lui si apoi ii ia lista de restaurante si o scrie detalii ei in fisiere text
for city in cities:

    file.write(f"{city} \n")
    print(city) # sa vezi ce oras scrie face acuma pentru ca dureaza mult lista

    responseR = requests.get(f"https://tazz.ro/{city}/restaurante")
    soupR = BeautifulSoup(responseR.content, 'html.parser')

    restaurant_list = soupR.find('div', {'class': 'partnersListLayout'})
    store_cards = restaurant_list.find_all('div', {'class': 'store-card'})

    file.write("Restaurant Livrare Stele \n")
    for store_card in store_cards:
        name = store_card.find('h3', {'class': 'store-name'})
        delivery_cost = store_card.find('div', {'class': 'store-delivery'})
        rating = store_card.find('div', {'class': 'store-rating'})
   
        #unele au atributele missing
        if rating is not None: 
            rating = rating.text.strip()
        else:
            rating = "None"

        if delivery_cost is not None:
            delivery_cost = delivery_cost.text.strip()
            delivery_cost = re.sub('[^0-9.]', '', delivery_cost) #filtreaza doar numarul sa fie, e regex am cautat pe net asta nus asa destept
        else:
            delivery_cost = "None"
        
        if name is not None:
            name = name.text.strip()
        else:
            name = "None"


        file.write(f"{name} {delivery_cost} {rating} \n")

file.close()
