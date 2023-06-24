import json
import requests
import scrappy_urls
from bs4 import BeautifulSoup

def connection(url):
    response = requests.get(url)
    html_content = response.content
    return html_content

def make_soup(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def get_areas(soup):
    '''
    Get the areas links to look for inside a type of contract. e. g. Medellin, Bello, Itagui, etc'''
    links = soup.find_all(class_="w3-btn w3-white w3-border w3-round-large")
    links = [tag.parent['href'] for tag in links]

    return links

def fetch_codes(soup):
    codes = []
    data = []

    areas_links = get_areas(soup)
    
    for areas in areas_links:
        codes_list = get_everything(areas)
        print(f"  - Appending {len(codes_list)} entries.")
        codes.append(codes_list)

    for sublist in codes:
        data.extend(sublist)

    return data

# Is this even needed? I think we can delete it
def get_everything(areas):
    codes = []
    data = []

    # for area in areas:
        # print('2nd. Getting\n' + area)
    code_list = get_entire_area(areas)
    codes.append(code_list)

    for sublist in codes:
        data.extend(sublist)

    return data
        

def get_entire_area(area):
    codes = []
    offset = 0
    current_page = 0
    
    current_area = area.split("nCiudad=")[1]

    url = "https://www.espaciourbano.com/" + area
    html_content = connection(url)
    soup = make_soup(html_content)
    pages_element = soup.find('a', string=lambda text: text and 'Página' in text)
    pages = pages_element.get_text()
    page_amount = int(pages.split("/ ")[1])

    print("\nScrapping", current_area)
    print("  - {area}")
    

    while current_page < page_amount:
        new_url = "https://www.espaciourbano.com/" + area + "&offset=" + str(offset)
        new_url = new_url.replace("%20", "+")
        html_content = connection(new_url)
        soup = make_soup(html_content)
        # TO DO: Find the page numbers, and write the function to iterate and:
        # 1. append codes
        # 2. go to next page
        property_links = soup.find_all(class_="btn btn-primary")
        print(f"    - {current_page + 1} / {page_amount}")

        for item in property_links:
            link = item['href']
            if '=' in link:
                link = link.replace(" ", "").split("=")[1]
                codes.append(link)
            else: 
                continue
        
        current_page += 1
        offset = 50 * current_page

    print("Finished", current_area)
    return codes

def secure_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print('Data saved to', filename)

def main():
    urls = scrappy_urls.main()

    codes = [] # Will be a list of lists
    data = [] # Will be a pure list

    for url in urls:
        print("\nCurrent URL: ", url)

        html_content = connection(url)
        soup = make_soup(html_content)
        codes.append(fetch_codes(soup))
    
    # Extending, as above loop returns a list of lists. This returns a single list
    for sublist in codes:
        data.extend(sublist)

    # Uncomment to save codes in file
    # filename = "codes.json"
    # secure_data(data, filename)


    print("Returned", len(data), "entries.")

    return data

# Run
if __name__ == "__main__":
    main()