import json
import requests
from time import perf_counter
from bs4 import BeautifulSoup

'''TO DO
- [] Way to download images (should be done uppon request)
- [x] Another script to scrap all urls
- [] Get something to do with the data'''

# Pending to learn about classes and nest everything appropriatedly 
class Scrappy():
    pass

# Connect to the page
def connection(url):
    response = requests.get(url)
    html_content = response.content
    return html_content

# Prepare the soup
def make_soup(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

# Get the data
def fetch_data(soup):
    apt_data = {}
    apt_data['Código'] = fetch_code(soup)
    apt_data['Tipo propiedad'] = fetch_property_type(soup)
    apt_data['Tipo contrato'], apt_data['Precio'] = fetch_type_price(soup)
    apt_data['Descripción'] = fetch_description(soup)
    apt_data.update(fetch_table(soup))
    apt_data['Comodidades'] = fetch_amenities(soup)
    apt_data['Agencia'] = fetch_agency(soup)

    return apt_data

# Get the apartment code & neighborhood
def fetch_code(soup):
    apt_code = soup.find('div', class_='text-center').h3.p.text.strip()
    code = apt_code.split('/')[0]
    code = ''.join(filter(str.isdigit, code)) # Getting it to output the numbers only
    return code

def fetch_property_type(soup):
    title = soup.title.text.strip()
    property_type = title.split(' en')[0]
    return property_type

# Get the apartment price
def fetch_type_price(soup):
    price_element = soup.find('div', class_='text-center').h3.find_next('h3')
    price_text = price_element.text.strip()
    price = price_text.split('$')[1]
    transaction = price_text.split(' $')[0]
    return transaction, price

def fetch_description(soup):
    description_element = soup.find('div', class_='container', align='justify')
    description = description_element.text.strip()
    return description

def fetch_amenities(soup):
    amenities = {}
    current_key = None
    container = soup.find('div', class_='col-lg-4')
    
    for element in container.find_all(['h3', 'p']):
        if element is not None:
            if element.name == 'h3':
                current_key = element.text.strip()
                amenities[current_key] = []
            elif element.name == 'p' and current_key:
                amenities[current_key].append(element.find('span').text.strip())

    return amenities

def fetch_table(soup):
    table = soup.find(class_="table table-striped")
    data = {}
    if table is not None:
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 2:
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                data[key] = value
    return data

def fetch_agency(soup):
    card = soup.find(class_='card')
    agency = {}
    phone_numbers = []
    agent = card.find(class_='card-title').text.strip()
    agency_name = card.find(class_='card-text').text.strip()
    for phone in card.find_all('p'):
        phone_icon = phone.find('i', class_='fas fa-phone-volume')
        if phone_icon:
            number = phone.text.strip()
            phone_numbers.append(number)
    agency['Agente'] = agent
    agency['Nombre agencia'] = agency_name
    agency['Contacto agente'] = phone_numbers
    return agency

# Save the data in a file
def secure_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print('Data saved to', filename)

# Outline
def main(url):
    t1_start = perf_counter()
    html_content = connection(url)
    soup = make_soup(html_content)
    data = fetch_data(soup)
    t2_stop = perf_counter()
    print(" ", t2_stop - t1_start)
    
    # Uncomment to save data in a .json
    # filename = "property_data.json"
    # secure_data(data, filename)
    return data
    

# Run
if __name__ == "__main__":
    main()
