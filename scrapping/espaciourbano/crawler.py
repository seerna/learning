# used to crawl the apts data.
# Objectives: Find links.
#     1. [x] Find all apartments & studies from desired areas, and under the desired budget
#     2. Create menus to filter using tkinter buttons. Output will be displayed on the console. There will be an export button for urls.


import json


def fetch_data():
    filename = "main_data.json"
    with open(filename , "r") as data:
        full_data = json.load(data)

    return full_data


def find_keys(full_data):
    key_list = full_data[0].keys()
    
    print('Keys:\n')
    for key in key_list:
        print(key)


def find_items(full_data, key):
    items = set()

    print('\nItems for:', key)
    for item in full_data:
        i = item[key]
        items.add(i)
    print(items)


def findby_key(full_data, key, items):
    filtered_data = []
    filter_by = items
    for item in full_data:
        if item[key] in filter_by:
            filtered_data.append(item)
    return filtered_data

def filterby_price(data, price_cap):
    filtered_data = []
    for item in data:
        price = item['Precio']
        price = price.replace(",","")
        if int(price) <= int(price_cap):
            filtered_data.append(item)

    return filtered_data

def get_links(data):
    urls = []
    url_base = 'https://www.espaciourbano.com/Ficha.asp?xId='
    for item in data:
        code = item['Código']
        urls.append(url_base + code)
    return urls

def main():
    full_data = fetch_data()

    # find_keys(full_data)
    # find_items(full_data)

    properties = ["Apartamento", "Apartaestudio", "Finca"]
    # cities = ["Medellin Zona 4 - Belen", "Medellin Zona 3 - Laureles", "Medellin Zona 2 - El Poblado"]
    cities = ["Sabaneta"]
    price_cap = 1000000

    # filtered_data = findby_key(full_data, "Tipo propiedad", properties)
    filtered_data = findby_key(full_data, "Ciudad", cities)
    # filtered_data = filterby_price(filtered_data, price_cap)

    find_items(filtered_data, "Ciudad")

    print("\n" + str(len(filtered_data)), "available properties.\n")

    links = get_links(filtered_data)
    for link in links:
        print(link)

if __name__ == "__main__":
    main()