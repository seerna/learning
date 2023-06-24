import json
import scrappy_codes
import scrappy_info

def fetch_urls():
    codes = scrappy_codes.main()
    urls = []
    for code in codes:
        url_base = 'https://www.espaciourbano.com/Ficha.asp?xId='
        urls.append(url_base + code)
    return urls

def secure_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print('Data saved to', filename)

def main():
    data = []
    urls = fetch_urls()

    for url in urls:
        try:
            data.append(scrappy_info.main(url))
            print(f"Scrapped {len(data)}/{len(urls)}.")
        except AttributeError:
            continue

    filename = "main_data.json"
    secure_data(data, filename)
    
if __name__ == "__main__":
    main()