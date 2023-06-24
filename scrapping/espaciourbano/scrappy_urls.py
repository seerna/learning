import json
import requests
from bs4 import BeautifulSoup

'''TO DO
- [x] Find a way to locate the list pages
- [] Find a way to navigate through the pages while fetching the urls'''

def connection(url):
    response = requests.get(url)
    html_content = response.content
    return html_content

def make_soup(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def fetch_data(soup):    
    half_urls = fetch_half_urls(soup)
    urls = get_urls(half_urls)
    return urls

def fetch_half_urls(soup):
    half_urls = []
    content = soup.find_all(class_="dropdown-item")
    # content = soup.find(string="Para Arrendar")
    for rows in content:
        # type_property = rows.text.strip()
        link = rows["href"]
        half_urls.append(link)
        # transaction = fetch_transaction(link)
    return half_urls

def fetch_transaction(link):
    start_index = link.index('_') + 1
    end_index = link.index('.')
    transaction = link[start_index:end_index]
    return transaction

def get_urls(half_urls):
    urls = []
    for half in half_urls:
        urls.append("http://www.espaciourbano.com/" + half)
    return urls

def secure_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print('Data saved to', filename)

def filter_urls(data):
    filtered_data = []
    for link in data:
        if "listado_arriendos" in link:
            filtered_data.append(link)
    
    return filtered_data

# Outline
def main():
    url = 'https://www.espaciourbano.com/'
    html_content = connection(url)
    soup = make_soup(html_content)
    data = fetch_data(soup)
    data = filter_urls(data)
    # filename = "links.json"
    # secure_data(data, filename)
    print(f"\nReturned: {len(data)}\n", data)
    return data

# Run
if __name__ == "__main__":
    main()