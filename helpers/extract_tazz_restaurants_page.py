import requests


def get_tazz_restaurants_page():
    tazz_response = requests.get("https://tazz.ro/cluj-napoca/restaurante")
    with open("tazz.html", 'wb') as html_file:
        html_file.write(tazz_response.content)


get_tazz_restaurants_page()
