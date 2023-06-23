# used to crawl the apts data.

import json


def fetch_data():
    filename = "main_data.json"
    with open(filename , "r") as data:
        full_data = json.load(data)

    return full_data

def find_code(full_data):
    pass

def main():
    full_data = fetch_data()
    find_code(full_data)
    print(type(full_data[0].keys()))

if __name__ == "__main__":
    main()