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

def fetch_data(soup):
    codes = fetch_codes(soup)
    return codes

def fetch_codes(soup):
    codes = []
    element = soup.find_all(class_="btn btn-primary")
    for item in element:
        link = item['href']
        if '=' in link:
            link = link.replace(" ", "").split("=")[1]
            codes.append(link)
        else: 
            continue
    return codes

def secure_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print('Data saved to', filename)

def main():
    urls = scrappy_urls.main()
    codes = []
    data = []
    for url in urls:
        html_content = connection(url)
        soup = make_soup(html_content)
        codes.append(fetch_data(soup))
    
    for sublist in codes:
        data.extend(sublist)

    # Uncomment to save codes in file
    # filename = "codes.json"
    # secure_data(data, filename)
    return data

# Run
if __name__ == "__main__":
    main()